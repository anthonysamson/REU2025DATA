import pandas as pd
from collections import defaultdict

# load and clean CSV
df = pd.read_csv("results.csv")
df.columns = df.columns.str.strip().str.lower()
df['configid'] = df['configid'].str.strip().str.lower()
df['status'] = df['status'].str.strip().str.upper()

# solver groups
soplex_configs = ['c1','c2','c3','c4','c5','c6','c7']
qsopt_config = 'c8'

# track counts and ratios
best_config_counts = defaultdict(int)
config_ratios = defaultdict(list)

# group by problem
for problem, group in df.groupby('file'):
    configs_present = set(group['configid'])
    if not configs_present >= set(soplex_configs + [qsopt_config]):
        continue  # skips incomplete problems

    c8_row = group[(group['configid'] == qsopt_config) & (group['status'] == 'OPTIMAL')]
    if c8_row.empty:
        continue

    c8_time = c8_row['timeseconds'].values[0]
    if c8_time <= 60:
        continue  # only interested in slow problems

    # get SoPlex config rows with OPTIMAL status
    soplex_rows = group[(group['configid'].isin(soplex_configs)) & (group['status'] == 'OPTIMAL')]

    if soplex_rows.empty:
        continue

    # find the SoPlex config with the minimum time
    best_row = soplex_rows.loc[soplex_rows['timeseconds'].idxmin()]
    best_config = best_row['configid']
    best_time = best_row['timeseconds']

    # record count and ratio
    best_config_counts[best_config] += 1
    config_ratios[best_config].append(best_time / c8_time)

# output results
print("Most Comparable SoPlex Configs on C8 > 60s Problems:\n")
for config in sorted(best_config_counts.keys()):
    count = best_config_counts[config]
    avg_ratio = sum(config_ratios[config]) / len(config_ratios[config])
    print(f"{config.upper()}: fastest on {count} problems, avg ratio to C8 = {avg_ratio:.2f}×")

# identify most comparable config
most_comparable = min(config_ratios.items(), key=lambda x: sum(x[1])/len(x[1]))[0]
print(f"\nMost comparable to QSopt_ex (on slow problems): {most_comparable.upper()}")
