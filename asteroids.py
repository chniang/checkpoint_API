import requests
import pandas as pd

api_key = "lqlmxg4mnC5vbrMwt5Tn2oksg34exwXVIawIHkAk"
url = "https://api.nasa.gov/neo/rest/v1/feed"

params = {
    "start_date": "2024-06-01",
    "end_date": "2024-06-02",
    "api_key": api_key
}

response = requests.get(url, params=params)
data = response.json()

asteroids = []
for date in data["near_earth_objects"]:
    for ast in data["near_earth_objects"][date]:
        asteroids.append({
            "ID": ast["id"],
            "Nom": ast["name"],
            "Diamètre (km)": ast["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
            "Magnitude": ast["absolute_magnitude_h"],
            "Vitesse (km/s)": ast["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]
        })

df = pd.DataFrame(asteroids)
df.to_csv("asteroides_nasa.csv", index=False)
print("CSV exporté.")
