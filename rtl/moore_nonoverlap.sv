module seq_detect (
    input  logic i_clk,
    input  logic i_rstn,
    input  logic i_data,
    output logic o_detect
);

logic [2:0] state, next_state;

localparam S0 = 3'd0,
           S1 = 3'd1,
           S2 = 3'd2,
           S3 = 3'd3,
           S4 = 3'd4;

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
        S3: next_state = i_data ? S4 : S0;
        S4: next_state = i_data ? S1 : S0;
        default: next_state = S0;
    endcase
end

assign o_detect = (state == S4);

`ifndef DISABLE_WAVES
initial begin
    $dumpfile("./sim_build/seq_detect.vcd");
    $dumpvars(0, seq_detect);
end
`endif

endmodule
