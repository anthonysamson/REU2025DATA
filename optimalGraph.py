import pandas as pd
import matplotlib.pyplot as plt

# load and clean data
df = pd.read_csv("results.csv")
df.columns = df.columns.str.strip().str.lower()
df['configid'] = df['configid'].str.strip().str.lower()
df['status'] = df['status'].str.strip().str.upper()

# filter to only C1–C8
filtered = df[df['configid'].isin(['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'])]

# count OPTIMAL statuses per config
optimal_counts = filtered[filtered['status'] == 'OPTIMAL']['configid'].value_counts().sort_index()

# generate alternating colors
bar_colors = ['#FAC800' if i % 2 == 0 else 'black' for i in range(len(optimal_counts))]

# create the plot
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor('#ff0000ff')  
ax.set_facecolor('#ff0000ff')        

# plot the bar chart
optimal_counts.plot(kind='bar', color=bar_colors, edgecolor='black', ax=ax)

# customize appearance
plt.title("Number of Optimal Solutions Found per Config", color='white')
plt.ylabel("Optimal Solutions Found", color='white')
plt.xlabel("Configuration", color='white')
plt.xticks(rotation=0, color='white')
plt.yticks(color='white')
plt.grid(axis='y', linestyle='--', linewidth=0.5, color='white')

plt.tight_layout()
plt.show()
