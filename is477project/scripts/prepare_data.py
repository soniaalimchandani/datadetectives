import sys
import pandas as pd
import os

complaints_path = sys.argv[1]
energy_path = sys.argv[2]
out_path = sys.argv[3]

os.makedirs(os.path.dirname(out_path), exist_ok=True)

complaints_df = pd.read_csv(complaints_path)
energy_df = pd.read_csv(energy_path)

# rename
energy_df = energy_df.rename(columns={
    "Latitude": "energy_lat",
    "Longitude": "energy_lon"
})

complaints_df = complaints_df.rename(columns={
    "LATITUDE": "complaint_lat",
    "LONGITUDE": "complaint_lon"
})

# rounding
energy_df["lat_round"] = energy_df["energy_lat"].round(3)
energy_df["lon_round"] = energy_df["energy_lon"].round(3)

complaints_df["lat_round"] = complaints_df["complaint_lat"].round(3)
complaints_df["lon_round"] = complaints_df["complaint_lon"].round(3)

# merge
merged_df = pd.merge(
    complaints_df,
    energy_df,
    on=["lat_round", "lon_round"],
    how="inner"
)

merged_df = merged_df.drop(columns=["lat_round", "lon_round"])

merged_df.to_csv(out_path, index=False)

print("Merged dataset created:", merged_df.shape)