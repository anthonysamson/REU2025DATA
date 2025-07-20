import pandas as pd
import matplotlib.pyplot as plt

# load your CSV file
df = pd.read_csv("results.csv")

# clean up columns
df.columns = df.columns.str.strip().str.lower()
df['configid'] = df['configid'].str.strip().str.lower()

# filter: only C1–C7 and time ≤ 750 seconds
filtered = df[
    (df['configid'].isin(['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'])) &
    (df['timeseconds'] <= 750)
]

# compute average solve time per config
avg_times = filtered.groupby('configid')['timeseconds'].mean().sort_values()

# identify the best (fastest) config
fastest_config = avg_times.idxmin()
fastest_time = avg_times.min()

# set bar colors: black for fastest, #FAC800 for others
colors = ['black' if cid == fastest_config else '#FAC800' for cid in avg_times.index]

# create the plot
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor('#ff0000ff')  
ax.set_facecolor('#ff0000ff')       

# plot the data
avg_times.plot(kind='bar', color=colors, edgecolor='black', ax=ax)

# annotate and style
plt.title("Average Solve Time (C1–C8, excluding time > 750s)", color='white')
plt.ylabel("Average Time (seconds)", color='white')
plt.xlabel("Configuration", color='white')
plt.xticks(rotation=0, color='white')
plt.yticks(color='white')
plt.grid(axis='y', linestyle='--', linewidth=0.5, color='white')
plt.text(avg_times.index.get_loc(fastest_config), fastest_time + 0.05,
         "Fastest", ha='center', fontsize=9, fontweight='bold', color='white')

plt.tight_layout()
plt.show()
