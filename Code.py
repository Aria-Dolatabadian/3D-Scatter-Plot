import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("yiled components.csv")

# Scatter Plot
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection="3d")
scatter = ax.scatter3D(df['Plant number'], df['Seed number'], df['Seed weight'],
                       c=df['Cultivar'], s=df['Yield']/50, alpha=0.4)

# Create a legend
legend_labels = df['Cultivar'].unique()
handles, labels = scatter.legend_elements()
ax.legend(handles, legend_labels, title='Cultivar')

ax.set_xlabel("Plant number")
ax.set_ylabel("Seed number")
ax.set_zlabel("Seed weight")
ax.set_title("Investigating the relationship between seed weight, seed number, and plant number on seed yield across four cultivars")

plt.show()
