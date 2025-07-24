import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# load and clean data
df = pd.read_csv("results.csv")
df.columns = df.columns.str.strip().str.lower()
df['configid'] = df['configid'].str.strip().str.lower()
df['status'] = df['status'].str.strip().str.upper()

# filter to configs C1–C8
filtered = df[df['configid'].isin(['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'])]

# count OPTIMAL status per config
optimal_counts = (
    filtered[filtered['status'] == 'OPTIMAL']['configid']
    .value_counts()
    .sort_index()
)

# rename 'c8' to 'q1'
optimal_counts.index = ['q1' if x == 'c8' else x for x in optimal_counts.index]

# identify the config with the most optimal solutions
max_val = optimal_counts.max()
bar_colors = ['#FAC800' if val == max_val else '#ff0000ff' for val in optimal_counts]

# plotting
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_alpha(0.0)       
ax.set_facecolor("none")      

# create bar plot
optimal_counts.plot(kind='bar', color=bar_colors, edgecolor='black', ax=ax)

# text formatting
ax.set_title("Number of Optimal Solutions Found per Config", color='white')
ax.set_ylabel("Optimal Solutions Found (48 Tested Total)", color='white')
ax.set_xlabel("Configuration", color='white')
ax.tick_params(axis='x', colors='white', rotation=0)
ax.tick_params(axis='y', colors='white')

# gridlines
ax.grid(axis='y', linestyle='--', linewidth=0.5, color='gray')

plt.tight_layout()
plt.show()
