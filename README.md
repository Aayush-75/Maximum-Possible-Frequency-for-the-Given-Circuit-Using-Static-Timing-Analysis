This paper presents an in-depth investigation of static timing analysis (STA) applied to digital circuits for determining the maximum operating frequency. We explore key timing parameters such as propagation delay, setup and hold times, and critical path determination. A Python-based approach is used to automate the STA process by analyzing digital netlists. The methodology includes recursive path tracing and delay computation to identify bottlenecks. Simulation results confirm the theoretical findings, with our test circuit achieving a maximum frequency of 0.0435 Hz.
This project computes the maximum achievable clock frequency (or minimum clock period) of a synchronous digital circuit using Static Timing Analysis (STA)—a method that identifies critical timing paths without full logic simulation

Data paths vs. clock paths

Data paths run from a flip‑flop’s clock‑to‑Q output to another flip‑flop’s data input, traversing combinational logic.

Clock paths model skew/buffer delays from the clock source to each flip‑flop’s clock pin 
vlsi-expert.com
+1
Electronics Hub
+1
Wikipedia
+1
vlsiuniverse.com
+1
.

Timing constraints:

Setup constraint (max‑time):
Tclk‑q
+
Tcomb,max
+
Tsetup
≤
𝑇
clk
+
Tclk‑skew,min
Tclk‑q+Tcomb,max+Tsetup≤T 
clk
​
 +Tclk‑skew,min

Hold constraint (min‑time):
Tclk‑q
+
Tcomb,min
≥
Thold
+
Tclk‑skew,max
Tclk‑q+Tcomb,min≥Thold+Tclk‑skew,max

Calculating maximum frequency:
The critical (worst-case) setup constraint happens when the data path delay is maximal and the clock path delay is minimal. Thus:

\begin{aligned} T_{\text{clk,min}} &= \text{Tclk‑q} + \max(\text{Tcomb,max}) - \min(\text{Tclk_skew}) + \text{Tsetup} \\ f_{\text{max}} &= \frac{1}{T_{\text{clk,min}}} \end{aligned}

This matches standard STA formulations
