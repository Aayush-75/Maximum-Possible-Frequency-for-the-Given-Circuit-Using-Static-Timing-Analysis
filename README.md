This paper presents an in-depth investigation of static timing analysis (STA) applied to digital circuits for determining the maximum operating frequency. We explore key timing parameters such as propagation delay, setup and hold times, and critical path determination. A Python-based approach is used to automate the STA process by analyzing digital netlists. The methodology includes recursive path tracing and delay computation to identify bottlenecks. Simulation results confirm the theoretical findings, with our test circuit achieving a maximum frequency of 0.0435 Hz.

Objective:
Determine the maximum clock frequency (or minimum clock period) for a synchronous circuit using Static Timing Analysis (STA).

1. 📐 Key Concepts
Timing paths:

Data-paths: From a flip‑flop’s clock‑to‑Q output, through combinational logic, to the next flip‑flop’s D input.

Clock‑paths: From the clock source to each flip‑flop's clock pin, including buffering/skew effects.

Timing constraints:

Setup:
T_{\text{clk‑q}} + T_{\text{comb,max}} + T_{\text{setup}} \le T_{\text{clk}} + T_{\text{clk‑skew,min}} \]

Hold:
T_{\text{clk‑q}} + T_{\text{comb,min}} \ge T_{\text{hold}} + T_{\text{clk‑skew,max}} \]
