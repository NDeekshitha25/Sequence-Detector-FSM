# Sequence Detector FSM

A SystemVerilog implementation of a **1111 sequence detector** using finite state machines (FSMs). The repository includes both **Moore** and **Mealy** models with **overlapping** and **non-overlapping** sequence detection, along with a Cocotb-based verification testbench.

## Repository Structure

```
Sequence-Detector-FSM/
├── rtl/
│   ├── mealy_nonoverlap.sv
│   ├── mealy_overlap.sv
│   ├── moore_nonoverlap.sv
│   └── moore_overlap.sv
├── tb/
│   └── test_seq_detector.py
├── .gitignore
├── LICENSE
└── README.md
```

## Features

- Detects the binary sequence **1111**
- Moore FSM implementation
- Mealy FSM implementation
- Overlapping sequence detection
- Non-overlapping sequence detection
- Synchronous FSM design using `always_ff` and `always_comb`
- Active-low asynchronous reset
- Cocotb-based functional verification

## Implementations

| File | FSM Type | Overlapping |
|------|----------|-------------|
| `moore_overlap.sv` | Moore | Yes |
| `moore_nonoverlap.sv` | Moore | No |
| `mealy_overlap.sv` | Mealy | Yes |
| `mealy_nonoverlap.sv` | Mealy | No |

## Verification

The repository includes a Cocotb testbench that applies a predefined input sequence and automatically distinguishes between the four FSM implementations based on their output patterns.

The testbench verifies:
- Moore FSM (Overlapping)
- Moore FSM (Non-overlapping)
- Mealy FSM (Overlapping)
- Mealy FSM (Non-overlapping)

Waveforms are dumped as VCD files for debugging and can be viewed using GTKWave or any compatible waveform viewer.

## Tools Used

- SystemVerilog
- Cocotb
- Icarus Verilog / ModelSim / Vivado Simulator
- GTKWave

## Learning Outcomes

- Finite State Machine (FSM) design
- Moore vs Mealy architectures
- Overlapping vs Non-overlapping sequence detection
- RTL design using SystemVerilog
- Functional verification using Cocotb
- Digital design simulation and waveform analysis

## License

This project is licensed under the MIT License.
