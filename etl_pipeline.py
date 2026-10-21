import os
import sqlite3
import requests
import pandas as pd

CITIES = {
    "Chennai": (13.08, 80.27),
    "Delhi": (28.61, 77.21),
    "Mumbai": (19.08, 72.88),
    "Bengaluru": (12.97, 77.59),
    "Kolkata": (22.57, 88.36),
}
URL = "https://air-quality-api.open-meteo.com/v1/air-quality"


def extract():
    frames = []
    for city, (lat, lon) in CITIES.items():
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "pm10,pm2_5,ozone,nitrogen_dioxide",
            "past_days": 90,
            "timezone": "Asia/Kolkata",
        }
        data = requests.get(URL, params=params).json()
        df = pd.DataFrame(data["hourly"])
        df["city"] = city
        frames.append(df)
    raw = pd.concat(frames, ignore_index=True)
    os.makedirs("data/raw", exist_ok=True)
    raw.to_csv("data/raw/air_quality_raw.csv", index=False)
    return raw


def transform(df):
    df = df.copy()
    df["time"] = pd.to_datetime(df["time"])
    df["date"] = df["time"].dt.date.astype(str)
    df["hour"] = df["time"].dt.hour
    df["month"] = df["time"].dt.month_name()
    df["pm25_category"] = pd.cut(
        df["pm2_5"],
        bins=[-1, 30, 60, 90, 120, 250, 1000],
        labels=["Good", "Satisfactory", "Moderate", "Poor", "Very Poor", "Severe"],
    ).astype(str)
    df = df.drop_duplicates(subset=["city", "time"])
    os.makedirs("data/clean", exist_ok=True)
    df.to_csv("data/clean/air_quality_clean.csv", index=False)
    return df


def load(df):
    conn = sqlite3.connect("air_quality.db")
    df.to_sql("air_quality", conn, if_exists="replace", index=False)
    conn.close()


if __name__ == "__main__":
    raw = extract()
    print("Extracted:", raw.shape)
    clean = transform(raw)
    print("Transformed:", clean.shape)
    load(clean)
    print("Loaded into air_quality.db")
    
