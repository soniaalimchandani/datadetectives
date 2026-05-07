import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

inp = sys.argv[1]
out_txt = sys.argv[2]
out_plot1 = sys.argv[3]
out_plot2 = sys.argv[4]

os.makedirs(os.path.dirname(out_txt), exist_ok=True)

df = pd.read_csv(inp)

# ----------------------------
# Assign neighborhoods
# ----------------------------
def assign_neighborhood(lat, lon):
    if (41.867 < lat <= 41.891) and (-87.640 <= lon <= -87.610):
        return "The Loop"
    elif (41.845 <= lat <= 41.867):
        return "Near South Side"
    elif (41.891 < lat <= 41.910):
        return "Near North Side"
    elif (41.910 < lat <= 41.940):
        return "Lincoln Park"
    elif (41.910 <= lat <= 41.935):
        return "Logan Square"
    elif (41.885 <= lat <= 41.910):
        return "West Town"
    elif (41.865 <= lat <= 41.885):
        return "Near West Side"
    elif (41.780 <= lat <= 41.805):
        return "Hyde Park"
    elif (41.760 <= lat <= 41.795):
        return "Englewood"
    elif (41.820 <= lat <= 41.850):
        return "Bridgeport"
    return "Other"

df["neighborhood"] = df.apply(
    lambda x: assign_neighborhood(x["complaint_lat"], x["complaint_lon"]),
    axis=1
)

df_neighborhoods = df[df["neighborhood"] != "Other"].copy()

# ----------------------------
# Aggregation
# ----------------------------
neigh_stats = df_neighborhoods.groupby("neighborhood").agg({
    "ADDRESS": "count",
    "ENERGY STAR Score": "mean"
}).reset_index()

neigh_stats.columns = ["Neighborhood", "Complaint_Count", "Avg_Energy_Score"]

# ----------------------------
# Save summary stats
# ----------------------------
with open(out_txt, "w") as f:
    f.write(str(neigh_stats))

# ----------------------------
# Plot 1: bar + line
# ----------------------------
fig, ax1 = plt.subplots(figsize=(12, 6))

sns.barplot(x="Neighborhood", y="Complaint_Count", data=neigh_stats, ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)

ax2 = ax1.twinx()
sns.lineplot(x="Neighborhood", y="Avg_Energy_Score", data=neigh_stats, ax=ax2, marker="o")

plt.tight_layout()
plt.savefig(out_plot1)
plt.close()

# ----------------------------
# Plot 2: map (static export)
# ----------------------------
fig2 = px.scatter_mapbox(
    df_neighborhoods,
    lat="complaint_lat",
    lon="complaint_lon",
    color="neighborhood",
    zoom=10,
    height=700
)

fig2.update_layout(mapbox_style="carto-positron")

fig2.write_html(out_plot2)