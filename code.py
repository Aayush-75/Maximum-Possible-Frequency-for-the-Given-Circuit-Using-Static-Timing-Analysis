import pandas as pd
import numpy as np

input_csv = r"C:\SEM 6\TVDC\special assingment\input_csv.csv"
output_csv = r"C:\SEM 6\TVDC\special assingment\output_csv.csv"

df = pd.read_csv(input_csv)

net_delay = {int(row["net No."]): row["delay"] for _, row in df.iterrows()}

paths = []

def to_int(x):
    if isinstance(x, np.generic):
        x = x.item()
    if isinstance(x, float):
        return int(x)
    return x

def trace_net(net, current_path, primary_num):
    net = to_int(net)
    row = df[df["net No."] == net]
    if row.empty:
        return
    row = row.iloc[0]
    current_path.append(net)
    net_type = row["type"]
    if net_type == "inpt":
        paths.append([to_int(primary_num)] + current_path)  
        return
    elif net_type == "from":
        next_net = row["fanout"]
        trace_net(next_net, current_path, primary_num)
    elif net_type in ["nand", "nor", "and", "or", "xor", "xnor"]:
        fanin1 = row["fanin1"]
        fanin2 = row["fanin2"]
        trace_net(fanin1, current_path.copy(), primary_num)
        trace_net(fanin2, current_path.copy(), primary_num)
    elif net_type == "not":
        fanin1 = row["fanin1"]
        trace_net(fanin1, current_path.copy(), primary_num)
    else:
        return

for idx, row in df.iterrows():
    if row["fanout"] == 0:
        primary_number = row["net No."]
        trace_net(row["fanin1"], [], primary_number)
        trace_net(row["fanin2"], [], primary_number)

output_rows = []
frequencies = []

print("Traced paths with total delays and frequencies:")
for path in paths:
    total_delay = 0
    for net in path:
        total_delay += net_delay.get(net, 0)
    frequency = 1 / total_delay if total_delay != 0 else 0
    frequencies.append(frequency)
    print(f"{path} - [{total_delay}] - [{frequency:.4f}]")
    output_rows.append({
        "Path": path,
        "Total Delay": total_delay,
        "Frequency": round(frequency, 4)
    })

if frequencies:
    non_zero_frequencies = [f for f in frequencies if f > 0]
    if non_zero_frequencies:
        lowest_frequency = min(non_zero_frequencies)
        summary_text = f"maximum possible frequency for this circuit is: {lowest_frequency:.4f} Hz"
    else:
        summary_text = "No non-zero frequency computed."
else:
    summary_text = "No valid paths were traced."

print("\n" + summary_text)

output_df = pd.DataFrame(output_rows)
summary_row = pd.DataFrame({
    "Path": [summary_text],
    "Total Delay": [""],
    "Frequency": [""]
})
output_df = pd.concat([output_df, summary_row], ignore_index=True)
output_df.to_csv(output_csv, index=False)

print(f"\nOutput saved to {output_csv}")
