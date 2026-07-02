module seq_detect (
    input  logic i_clk,
    input  logic i_rstn,
    input  logic i_data,
    output logic o_detect
);

logic [1:0] state, next_state;

localparam S0 = 2'd0,
           S1 = 2'd1,
           S2 = 2'd2,
           S3 = 2'd3;

always_ff @(posedge i_clk or negedge i_rstn) begin
    if (!i_rstn)
        state <= S0;
    else
        state <= next_state;
end

always_comb begin
    case (state)
        S0: next_state = i_data ? S1 : S0;
        S1: next_state = i_data ? S2 : S0;
        S2: next_state = i_data ? S3 : S0;
        S3: next_state = i_data ? S0 : S0;
        default: next_state = S0;
    endcase
end

assign o_detect = (state == S3) && i_data;

`ifndef DISABLE_WAVES
initial begin
    $dumpfile("./sim_build/seq_detect.vcd");
    $dumpvars(0, seq_detect);
end
`endif

endmodule
