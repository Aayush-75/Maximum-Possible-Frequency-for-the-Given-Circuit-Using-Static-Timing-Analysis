This paper presents an in-depth investigation of static timing analysis (STA) applied to digital circuits for determining the maximum operating frequency. We explore key timing parameters such as propagation delay, setup and hold times, and critical path determination. A Python-based approach is used to automate the STA process by analyzing digital netlists. The methodology includes recursive path tracing and delay computation to identify bottlenecks. Simulation results confirm the theoretical findings, with our test circuit achieving a maximum frequency of 0.0435 Hz.

Objective:
Determine the maximum clock frequency (or minimum clock period) for a synchronous circuit using Static Timing Analysis (STA).

1. 📐 Key Concepts
Timing paths:

Data-paths: From a flip‑flop’s clock‑to‑Q output, through combinational logic, to the next flip‑flop’s D input.

Clock‑paths: From the clock source to each flip‑flop's clock pin, including buffering/skew effects.

Timing constraints:
1. Setup-Time Constraint
For every flip-flop-to-flip-flop path:

𝑇
𝑐
𝑞
+
𝑇
𝑐
𝑜
𝑚
𝑏
,
max
⁡
⏟
Data arrival
+
𝑇
𝑠
𝑒
𝑡
𝑢
𝑝
  
≤
  
𝑇
𝑐
𝑙
𝑘
+
𝑇
𝑠
𝑘
𝑒
𝑤
,
min
⁡
Data arrival
T 
cq
​
 +T 
comb,max
​
 
​
 
​
 +T 
setup
​
 ≤T 
clk
​
 +T 
skew,min
​
 

Rearranged to solve for minimum clock period:

𝑇
𝑐
𝑙
𝑘
,
min
⁡
=
𝑇
𝑐
𝑞
+
𝑇
𝑐
𝑜
𝑚
𝑏
,
max
⁡
+
𝑇
𝑠
𝑒
𝑡
𝑢
𝑝
−
𝑇
𝑠
𝑘
𝑒
𝑤
,
min
⁡
T 
clk,min
​
 =T 
cq
​
 +T 
comb,max
​
 +T 
setup
​
 −T 
skew,min
​
 

And max frequency:

𝑓
max
⁡
=
1
𝑇
𝑐
𝑙
𝑘
,
min
⁡
f 
max
​
 = 
T 
clk,min
​
 
1
​
 

This aligns with classic STA derivations 
sanjayvidhyadharan.in
+13
medium.com
+13
edn.com
+13
icdesigntips.com
+8
vlsi-expert.com
+8
en.wikipedia.org
+8
electronics.stackexchange.com
+5
edn.com
+5
southampton.ac.uk
+5
en.wikipedia.org
.

2. Hold-Time Constraint
To avoid capturing data too early:

𝑇
𝑐
𝑞
+
𝑇
𝑐
𝑜
𝑚
𝑏
,
min
⁡
⏟
Earliest data arrival
  
≥
  
𝑇
ℎ
𝑜
𝑙
𝑑
+
𝑇
𝑠
𝑘
𝑒
𝑤
,
max
⁡
Earliest data arrival
T 
cq
​
 +T 
comb,min
​
 
​
 
​
 ≥T 
hold
​
 +T 
skew,max
​
 

Or equivalently:

𝑇
𝑐
𝑞
+
𝑇
𝑐
𝑜
𝑚
𝑏
,
min
⁡
−
𝑇
𝑠
𝑘
𝑒
𝑤
,
max
⁡
  
≥
  
𝑇
ℎ
𝑜
𝑙
𝑑
T 
cq
​
 +T 
comb,min
​
 −T 
skew,max
​
 ≥T 
hold
​
 

This ensures the shortest data-path doesn’t violate hold timing 
