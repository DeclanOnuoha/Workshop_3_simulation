# analyze_results.py
import pandas as pd
import numpy as np
from scipy import stats
import os


def confidence_interval(data, conf=0.95):
    n = len(data)
    mean = np.mean(data)
    se = stats.sem(data)
    h = se * stats.t.ppf((1 + conf) / 2, n - 1)
    return mean, (mean - h, mean + h)


# Load data
files = ["3p4r", "3p5r", "4p5r"]
data = {f: pd.read_csv(f"results/{f}.csv") for f in files}

print("SURGERY SIMULATION ASSIGNMENT – FULL RESULTS")
print("=" * 60)

for name in files:
    df = data[name]
    q = df['queue_length']
    b = df['blocking_probability']
    r = df['rec_full_probability']

    print(f"\nConfiguration: {name.upper()}")
    print(f"  Avg queue length          : {confidence_interval(q)[0]:.4f}   95% CI {confidence_interval(q)[1]}")
    print(f"  Blocking probability      : {confidence_interval(b)[0]:.4f}   95% CI {confidence_interval(b)[1]}")
    print(f"  All recovery busy prob    : {confidence_interval(r)[0]:.4f}   95% CI {confidence_interval(r)[1]}")

# Paired comparisons (same seeds)
print("\nPAIRED DIFFERENCES (Common Random Numbers)")
q_diff = data["3p5r"]['queue_length'] - data["4p5r"]['queue_length']
b_diff = data["3p4r"]['blocking_probability'] - data["3p5r"]['blocking_probability']

print("Queue length: 3p5r − 4p5r :", confidence_interval(q_diff))
print("Blocking prob: 3p4r − 3p5r :", confidence_interval(b_diff))

# Relative precision
print("\nRELATIVE CONFIDENCE INTERVAL WIDTH")
for name in files:
    b = data[name]['blocking_probability']
    r = data[name]['rec_full_probability']
    rel_b = (confidence_interval(b)[1][1] - confidence_interval(b)[1][0]) / (2 * confidence_interval(b)[0])
    rel_r = (confidence_interval(r)[1][1] - confidence_interval(r)[1][0]) / (2 * confidence_interval(r)[0])
    print(f"{name}: Blocking rel. width = {rel_b:.3f} | All rec busy rel. width = {rel_r:.3f}")

print("\nConclusion: 'All recovery busy' usually has smaller relative CI when blocking is rare.")