import pandas as pd

# load and clean the CSV
df = pd.read_csv("results.csv")
df.columns = df.columns.str.strip().str.lower()
df['configid'] = df['configid'].str.strip().str.lower()

# prepare separate lists for <60s and >60s cases
avg_ratios_fast = []
min_ratios_fast = []

avg_ratios_slow = []
min_ratios_slow = []

# group by problem name
for problem, group in df.groupby("file"):
    configs = set(group['configid'])
    if configs >= set(['c1','c2','c3','c4','c5','c6','c7','c8']):
        c1_c7_times = group[group['configid'].isin(['c1','c2','c3','c4','c5','c6','c7'])]['timeseconds']
        c8_time = group[group['configid'] == 'c8']['timeseconds'].values[0]

        if c8_time > 0:
            avg_ratio = c1_c7_times.mean() / c8_time
            min_ratio = c1_c7_times.min() / c8_time

            if c8_time <= 60:
                avg_ratios_fast.append(avg_ratio)
                min_ratios_fast.append(min_ratio)
            else:
                avg_ratios_slow.append(avg_ratio)
                min_ratios_slow.append(min_ratio)

# compute and print results
print("=== Problems where C8 (QSopt_ex) took ≤ 60 seconds ===")
if avg_ratios_fast and min_ratios_fast:
    avg_speedup_fast = sum(avg_ratios_fast) / len(avg_ratios_fast)
    min_speedup_fast = sum(min_ratios_fast) / len(min_ratios_fast)
    print(f"Average speedup (SoPlex mean vs C8): {avg_speedup_fast:.2f}×")
    print(f"Average speedup (SoPlex best vs C8): {min_speedup_fast:.2f}×")
else:
    print("No qualifying problems in this category.")

print("\n=== Problems where C8 (QSopt_ex) took > 60 seconds ===")
if avg_ratios_slow and min_ratios_slow:
    avg_speedup_slow = sum(avg_ratios_slow) / len(avg_ratios_slow)
    min_speedup_slow = sum(min_ratios_slow) / len(min_ratios_slow)
    print(f"Average speedup (SoPlex mean vs C8): {avg_speedup_slow:.2f}×")
    print(f"Average speedup (SoPlex best vs C8): {min_speedup_slow:.2f}×")
else:
    print("No qualifying problems in this category.")
