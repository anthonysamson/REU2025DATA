import pandas as pd

# load and clean the CSV
df = pd.read_csv("results.csv") 
df.columns = df.columns.str.strip().str.lower()
df['configid'] = df['configid'].str.strip().str.lower()

avg_ratios = []
min_ratios = []

# group by problem name
for problem, group in df.groupby("file"):
    if set(group['configid']) >= set(['c1','c2','c3','c4','c5','c6','c7','c8']):
        c1_c7_times = group[group['configid'].isin(['c1','c2','c3','c4','c5','c6','c7'])]['timeseconds']
        c8_time = group[group['configid'] == 'c8']['timeseconds'].values[0]

        if c8_time > 0:
            avg_ratio = c1_c7_times.mean() / c8_time
            min_ratio = c1_c7_times.min() / c8_time
            avg_ratios.append(avg_ratio)
            min_ratios.append(min_ratio)

# compute overall averages
if avg_ratios and min_ratios:
    overall_avg_speedup = sum(avg_ratios) / len(avg_ratios)
    overall_min_speedup = sum(min_ratios) / len(min_ratios)

    print(f"On average, QSopt_ex is {overall_avg_speedup:.2f}× faster than the average of SoPlex.")
    print(f"On average, QSopt_ex is {overall_min_speedup:.2f}× faster than the fastest of SoPlex.")
else:
    print("No valid problem groups with all 8 configurations found.")
