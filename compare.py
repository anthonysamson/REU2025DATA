import matplotlib.pyplot as plt

# labels and values
labels = ['SoPlex Mean vs QSopt_ex', 'SoPlex Best vs QSopt_ex']
fast_values = [67.11, 19.67]
slow_values = [2.03, 1.34]
x = range(len(labels))
bar_width = 0.35

# create the plot
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor('#ff0000ff') 
ax.set_facecolor('#ff0000ff')         

# bar positions and colors
fast_bars = ax.bar(
    [i - bar_width/2 for i in x], fast_values, bar_width,
    label='C8 ≤ 60s', color='black' 
)
slow_bars = ax.bar(
    [i + bar_width/2 for i in x], slow_values, bar_width,
    label='C8 > 60s', color='#FAC800'
)

# labels and formatting
ax.set_ylabel('Speedup Ratio (SoPlex / QSopt_ex)', color='white')
ax.set_title('SoPlex Speedup Relative to QSopt_ex', color='white')
ax.set_xticks(x)
ax.set_xticklabels(labels, color='white')
ax.tick_params(colors='white')
ax.legend(facecolor='black', edgecolor='white', labelcolor='white')
ax.grid(axis='y', linestyle='--', linewidth=0.5, color='white')

# add bar annotations
for bars in [fast_bars, slow_bars]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}×',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='white', fontsize=9)

plt.tight_layout()
plt.show()
