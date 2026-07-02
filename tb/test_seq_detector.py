import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, FallingEdge, RisingEdge

data_in = "010011100110111001101111001111111100" # Test Sequence
moore_val = "000000000000000000000000100000111110"
mealy_val = "000000000000000000000001000001111100"
moore_val_non_overlapping = "000000000000000000000000100000100010"
mealy_val_non_overlapping = "000000000000000000000001000001000100"

def fsm_checker(output):
    if output==moore_val:
        cocotb.log.info(f"Hint: Moore FSM detected with overlapping sequence")
    elif output==mealy_val:
        cocotb.log.info(f"Hint: Mealy FSM detected with overlapping sequence")
    elif output==moore_val_non_overlapping:
        cocotb.log.info(f"Hint: Moore FSM detected with non-overlapping sequence")
    elif output==mealy_val_non_overlapping:
        cocotb.log.info(f"Hint: Mealy FSM detected with non-overlapping sequence")

@cocotb.test()
async def test_seq_detect(dut):

    t_clk = 1 # Clock period
    t_cq = 20 # clk -> q delay while driving the input


    # Initial Values
    dut.i_clk.value = 0
    dut.i_rstn.value = 0
    dut.i_data.value = 0

    data_detected= []
    await Timer(2, "ns")
    dut.i_rstn.value = 1

    # Start the clock at dut.i_clk Pin
    cocotb.start_soon(Clock(dut.i_clk, t_clk, units="ns").start())

    for val in data_in:
        # Drive data on Rising Edge
        await RisingEdge(dut.i_clk)

        await Timer(t_cq, "ps") # Optional wait emulating clk->q delay
        dut.i_data.value = int(val)

        # Sample the data on Falling Edge
        await FallingEdge(dut.i_clk)
        data_detected.append(dut.o_detect.value.binstr)

    data_out=''.join(data_detected)

    fsm_checker(data_out)

    # Use this if you're implementing Moore state-machine
    if data_out == moore_val:
        cocotb.log.info(f"detected in next cycle")
    else:
        cocotb.log.info(f"not detected, data_out = {data_out}, data_in = {data_in}")
        assert False

    # Use this if you're implementing Mealy state-machine
    # if data_out == mealy_val:
    #     cocotb.log.info(f"detected in same cycle")
    # else:
    #     cocotb.log.info(f"not detected, data_out= {data_out}, data_in= {data_in}")
    #     assert False
    
    await FallingEdge(dut.i_clk)
