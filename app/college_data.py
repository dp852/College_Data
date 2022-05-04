from webbrowser import get
import requests
import pandas as pd
from flask import Flask
from app.__init__ import APP_ENV

app = Flask(__name__)


def set_college():
    if APP_ENV == "development":
        qqq = input("PLEASE INPUT A 4-YEAR COLLEGE (e.g. 'US'): ")
    return qqq

def to_usd(data):
    return '${:,.2f}'.format(data)
def to_pct(data):
    return '{:.2%}'.format(data)
def to_int(data):
    return int(data)


def get_data(val):
    url = 'https://raw.githubusercontent.com/dp852/College_Data/main/Schools_data'
    df = pd.read_csv(url)
    df["school.name"] = df["school.name"].str.title()
    df["school.locale"] = df["school.locale"].replace([11, 12,13,21,22,23,31,32,33,41,42,43],['Large City', 'Midsize City', 'Small City', 'Large Suburb', 'Midsize Suburb', 'Small Suburb', 'Town Close to a city', 'Distant Town', 'Remote Town', 'Rural but Close to City', 'Distant Rural Area', 'Remote Rural Area'])
    df['latest.admissions.sat_scores.midpoint.math'] = df['latest.admissions.sat_scores.midpoint.math'].fillna(0)
    df['latest.admissions.sat_scores.midpoint.critical_reading'] = df['latest.admissions.sat_scores.midpoint.critical_reading'].fillna(0)
    df['latest.admissions.act_scores.midpoint.cumulative'] = df['latest.admissions.act_scores.midpoint.cumulative'].fillna(0)
    df['latest.admissions.admission_rate.overall'] = df['latest.admissions.admission_rate.overall'].fillna(0) 
    school_name = df["school.name"][df[df['school.name'] == val].index[0]]
    median_math_sat = to_int(df['latest.admissions.sat_scores.midpoint.math'][df[df['school.name'] == val].index[0]])
    median_verbal_sat = to_int(df['latest.admissions.sat_scores.midpoint.critical_reading'][df[df['school.name'] == val].index[0]])
    average_sat = median_math_sat+median_verbal_sat
    average_act = to_int(df['latest.admissions.act_scores.midpoint.cumulative'][df[df['school.name'] == val].index[0]])
    percent_white = to_pct(df['latest.student.demographics.race_ethnicity.white'][df[df['school.name'] == val].index[0]])
    percent_black =  to_pct(df['latest.student.demographics.race_ethnicity.black'][df[df['school.name'] == val].index[0]])
    percent_hispanic = to_pct(df['latest.student.demographics.race_ethnicity.hispanic'][df[df['school.name'] == val].index[0]])
    percent_asian = to_pct(df['latest.student.demographics.race_ethnicity.asian'][df[df['school.name'] == val].index[0]])
    acceptance_rate = to_pct(df['latest.admissions.admission_rate.overall'][df[df['school.name'] == val].index[0]])
    retention = to_pct(df['latest.student.retention_rate.four_year.full_time'][df[df['school.name'] == val].index[0]])
    enrollment = to_int(df['latest.student.size'][df[df['school.name'] == val].index[0]])
    location = df['school.locale'][df[df['school.name'] == val].index[0]]
    in_state = to_usd(df['latest.cost.tuition.in_state'][df[df['school.name'] == val].index[0]])
    out_state = to_usd(df['latest.cost.tuition.out_of_state'][df[df['school.name'] == val].index[0]])
    grad_rate = to_pct(df['latest.completion.completion_rate_4yr_100nt'][df[df['school.name'] == val].index[0]])
    salary_6 = to_usd(df['latest.earnings.6_yrs_after_entry.working_not_enrolled.mean_earnings'][df[df['school.name'] == val].index[0]])
    salary_8 = to_usd(df['latest.earnings.8_yrs_after_entry.mean_earnings'][df[df['school.name'] == val].index[0]])
    salary_10 = to_usd(df['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings'][df[df['school.name'] == val].index[0]])
    score = {"College": school_name, "Average SAT": average_sat, "Average Math SAT": median_math_sat, "Average Verbal SAT": median_verbal_sat, "Average ACT": average_act,
             "Acceptance Rate": acceptance_rate, "Retention Rate": retention, "Undergraduate Enrollment": enrollment, "Location": location, 
             "Percent White": percent_white, "Percent Black": percent_black, "Percent Asian": percent_asian, "Percent Hispanic": percent_hispanic,
             "In-state Tuition": in_state, "Out-of-state Tuition": out_state, "Graduation Rate": grad_rate, "Salary 6-years Post Entry": salary_6, 
             "Salary 8-years Post Entry": salary_8, "Salary 10-years Post-Entry": salary_10}
    return score



if __name__ == "__main__":

    school = set_college
    print("College:", school)
    
    result = get_data(school)

    



