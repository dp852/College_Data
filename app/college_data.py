import requests
import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route("/")
def fetch_data():
    url = 'https://raw.githubusercontent.com/dp852/College_Data/main/Schools_data'
    df = pd.read_csv(url)
    df["school.name"] = df["school.name"].str.lower()
    df["school.locale"] = df["school.locale"].replace([11, 12,13,21,22,23,31,32,33,41,42,43],['Large City', 'Midsize City', 'Small City', 'Large Suburb', 'Midsize Suburb', 'Small Suburb', 'Town Close to a city', 'Distant Town', 'Remote Town', 'Rural but Close to City', 'Distant Rural Area', 'Remote Rural Area'])
    df['latest.admissions.sat_scores.midpoint.math'] = df['latest.admissions.sat_scores.midpoint.math'].fillna(0)
    df['latest.admissions.sat_scores.midpoint.critical_reading'] = df['latest.admissions.sat_scores.midpoint.critical_reading'].fillna(0)
    df['latest.admissions.sat_scores.25th_percentile.math'] = df['latest.admissions.sat_scores.25th_percentile.math'].fillna(0)
    df['latest.admissions.sat_scores.25th_percentile.critical_reading'] = df['latest.admissions.sat_scores.25th_percentile.critical_reading'].fillna(0)
    df['latest.admissions.sat_scores.75th_percentile.math'] = df['latest.admissions.sat_scores.75th_percentile.math'].fillna(0)
    df['latest.admissions.sat_scores.75th_percentile.critical_reading'] = df['latest.admissions.sat_scores.75th_percentile.critical_reading'].fillna(0)
    df['latest.admissions.act_scores.midpoint.cumulative'] = df['latest.admissions.act_scores.midpoint.cumulative'].fillna(0)
    df['latest.admissions.act_scores.25th_percentile.cumulative'] = df['latest.admissions.act_scores.25th_percentile.cumulative'].fillna(0)
    df['latest.admissions.act_scores.75th_percentile.cumulative'] = df['latest.admissions.act_scores.75th_percentile.cumulative'].fillna(0)
    df['latest.admissions.admission_rate.overall'] = df['latest.admissions.admission_rate.overall'].fillna(0)
    return df

if __name__== "__main__":
    df=fetch_data()
    print(df.head)

