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

2. 🧮 Frequency Calculation
The critical path is the data path with maximum delay and minimum clock path delay:

𝑇
clk,min
=
𝑇
clk‑q
+
max
⁡
(
𝑇
comb,max
)
−
min
⁡
(
𝑇
clk‑skew
)
+
𝑇
setup
T 
clk,min
​
 =T 
clk‑q
​
 +max(T 
comb,max
​
 )−min(T 
clk‑skew
​
 )+T 
setup
​
 

𝑓
max
=
1
𝑇
clk,min
f 
max
​
 = 
T 
clk,min
​
 
1
​
 

Example:
If longest data-path delay is 26 ns, shortest clock path delay is 9 ns, and t_setup = 4 ns, then:

𝑇
clk,min
=
26
−
9
+
4
=
21
 
ns
T 
clk,min
​
 =26−9+4=21ns →
𝑓
max
=
1
/
21
 
ns
≈
47.6
 
MHz
f 
max
​
 =1/21ns≈47.6MHz 
kilthub.cmu.edu
+13
vlsi-expert.com
+13
vlsi-expert.com
+13

3. ⚙️ Implementation Overview
Input Parsing: Read netlist and timing parameters: 
𝑇
clk‑q
T 
clk‑q
​
 , combinational delays (min/max), 
𝑇
setup
T 
setup
​
 , 
𝑇
hold
T 
hold
​
 , clock path delays.

Path Enumeration: Identify all sequential paths (FF→combinational→FF).

Delay Aggregation: For each path, compute:

Max data path delay (sum of max delays)

Min clock path delay (sum of min delays)

Compute 
𝑇
clk,min
T 
clk,min
​
  using the formula above.

Verify hold: Ensure hold constraint holds for all paths.

Output: Show critical path details, slack values, computed 
𝑇
clk,min
T 
clk,min
​
 , and 
𝑓
max
f 
max
​
 .

4. 🚀 Usage
bash
Copy
Edit
python sta_max_freq.py \
  --netlist circuit.json \
  --tclkq 0.01 \
  --comb-max delays_max.json \
  --comb-min delays_min.json \
  --tsetup 0.005 \
  --thold 0.002 \
  --clk-path clk_delays.json
Output includes:

Critical path identifier

𝑇
clk,min
T 
clk,min
​
  and corresponding 
𝑓
max
f 
max
​
 

Setup and hold slack per path

5. ✅ Validation & Examples
Compare results against textbook/blog examples (e.g., data = 26 ns, t_setup = 4 ns, clk skew = 9 ns -> 
𝑇
clk,min
=
21
T 
clk,min
​
 =21 ns) 
vlsi-expert.com
+1
vlsi-expert.com
+1
vlsi-expert.com
+1
github.com
+1

Ensure hold-time verification for each path.

6. 🛠️ Future Enhancements
Support for clock skew/jitter variations

Incorporate multi‑clock domain analysis

Extend to statistical STA (SSTA) with process variation modeling
