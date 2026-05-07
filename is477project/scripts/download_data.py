import sys
import requests
import os

complaints_out = sys.argv[1]
energy_out = sys.argv[2]

os.makedirs(os.path.dirname(complaints_out), exist_ok=True)

datasets = {
    complaints_out: "https://data.cityofchicago.org/api/views/fypr-ksnz/rows.csv?accessType=DOWNLOAD",
    energy_out: "https://data.cityofchicago.org/api/views/3a36-5x9a/rows.csv?accessType=DOWNLOAD"
}

for path, url in datasets.items():
    response = requests.get(url)
    response.raise_for_status()

    with open(path, "wb") as f:
        f.write(response.content)

    print(f"Downloaded: {path}")