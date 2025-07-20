````markdown
# Maximum Clock Frequency Estimator 🕒🔍

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](#)

**Estimate the highest safe clock frequency** of any synchronous digital circuit using _Static Timing Analysis_ (STA).

---

## 🔖 Table of Contents
1. [📋 Overview](#-overview)
2. [📐 Key Concepts](#-key-concepts)
3. [🧮 Core Equations](#-core-equations)
4. [⚙️ Implementation Details](#️-implementation-details)
5. [🚀 Quickstart & Usage](#-quickstart--usage)
6. [📊 Example](#-example)
7. [✅ Validation](#-validation)
8. [🔮 Future Enhancements](#-future-enhancements)
9. [📄 License](#-license)

---

## 📋 Overview
This tool computes the **minimum clock period** (and thus the **maximum clock frequency**) for a synchronous circuit by:

- Parsing a circuit netlist and associated timing parameters
- Enumerating all FF→FF timing paths
- Aggregating worst-case data delays and best-case clock delays
- Verifying both setup and hold constraints via STA

Results help ensure timing closure without exhaustive simulation.

---

## 📐 Key Concepts

- **Data Path**: From flip‑flop `Q` output, through combinational logic, to flip‑flop `D` input.
- **Clock Path**: From clock source to FF clock pins, accounting for buffer/skew delays.
- **Setup Constraint**: Ensures data arrives before the next clock edge.
- **Hold Constraint**: Ensures data does not change too soon after a clock edge.

---

## 🧮 Core Equations
```text
# Setup-Time Constraint:
T_cq + T_comb,max + T_setup ≤ T_clk + T_skew,min

# ⇒ Minimum Clock Period:
T_clk_min = T_cq + T_comb,max + T_setup - T_skew,min

# ⇒ Maximum Frequency:
f_max = 1 / T_clk_min

# Hold-Time Constraint:
T_cq + T_comb,min ≥ T_hold + T_skew,max
````

---

## ⚙️ Implementation Details

1. **Input Parsing**: Read:

   * `T_cq`, `T_setup`, `T_hold`
   * Per-stage combinational delays (`max` & `min`)
   * Clock-path delays
   * Circuit netlist (FF connections)

2. **Path Enumeration**:

   * Traverse all sequential chains: FF → logic → FF

3. **Delay Aggregation**:

   * **Max Data Delay** = Σ `T_comb,max` along path
   * **Min Clock Delay** = Σ `T_clock_path,min`

4. **Clock Period Computation**:

   * Compute `T_clk_min` using the setup equation for each path
   * Identify **critical path** with largest `T_clk_min`

5. **Hold Verification**:

   * Ensure `T_cq + T_comb,min - T_skew,max ≥ T_hold` for every path

6. **Output**:

   * Critical path details
   * `T_clk_min`, `f_max`
   * Slack report (setup & hold)

---

## 🚀 Quickstart & Usage

1. **Clone the repo**

   ```bash
   git clone https://github.com/Aayush-75/Maximum-Possible-Frequency-for-the-Given-Circuit-Using-Static-Timing-Analysis.git
   cd Maximum-Possible-Frequency-for-the-Given-Circuit-Using-Static-Timing-Analysis
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run analysis**

   ```bash
   python sta_max_freq.py \
     --netlist     circuit.json \
     --tclkq       0.012 \
     --comb-max    delays_max.json \
     --comb-min    delays_min.json \
     --tsetup      0.004 \
     --thold       0.002 \
     --clk-path    clk_delays.json
   ```

4. **Interpret output**

   * `Critical Path`: Node sequence and delay sum
   * `T_clk_min` & `f_max` reported in ns & MHz
   * `Setup/Hold Slack` per path

---

## 📊 Example

```text
Critical Path: FF1 → L1 → L2 → FF2
T_cq = 0.012 ns, ΣT_comb,max = 25 ns,
T_setup = 0.004 ns, Min T_skew = 0.008 ns

T_clk_min = 0.012 + 25 - 0.008 + 0.004 = 25.008 ns
f_max = 1 / 25.008 ns ≈ 39.99 MHz
```

---

## ✅ Validation

* Matched textbook scenarios (e.g., 26 ns data, 9 ns skew, 4 ns setup → `T_clk_min`=21 ns)
* Verified hold constraints across multiple nets

---

## 🔮 Future Enhancements

* Clock jitter & skew variation modeling
* Multi‑clock domain analysis
* Statistical STA (SSTA) with process variation
* GUI for visualizing path delays

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

```
```
