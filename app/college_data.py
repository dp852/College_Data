import requests
import pandas as pd
from flask import Flask

app = Flask(__name__)

#@app.route("/")



def get_data(val):
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
    median_math_sat = int(df['latest.admissions.sat_scores.midpoint.math'][df[df['school.name'] == val].index[0]])
    median_verbal_sat = int(df['latest.admissions.sat_scores.midpoint.critical_reading'][df[df['school.name'] == val].index[0]])
    average_sat = median_math_sat+median_verbal_sat
    lower_math = int(df['latest.admissions.sat_scores.25th_percentile.math'][df[df['school.name'] == val].index[0]])
    lower_verbal = int(df['latest.admissions.sat_scores.25th_percentile.critical_reading'][df[df['school.name'] == val].index[0]])
    lower_sat = lower_math+lower_verbal
    upper_math = int(df['latest.admissions.sat_scores.75th_percentile.math'][df[df['school.name'] == val].index[0]])
    upper_verbal = int(df['latest.admissions.sat_scores.75th_percentile.critical_reading'][df[df['school.name'] == val].index[0]])
    upper_sat = upper_math + upper_verbal
    average_act = int(df['latest.admissions.act_scores.midpoint.cumulative'][df[df['school.name'] == val].index[0]])
    lower_act = int(df['latest.admissions.act_scores.25th_percentile.cumulative'][df[df['school.name'] == val].index[0]])
    upper_act = int(df['latest.admissions.act_scores.75th_percentile.cumulative'][df[df['school.name'] == val].index[0]])
    percent_white = "{:.2%}".format(df['latest.student.demographics.race_ethnicity.white'][df[df['school.name'] == val].index[0]], "%")
    percent_black =  "{:.2%}".format(df['latest.student.demographics.race_ethnicity.black'][df[df['school.name'] == val].index[0]], "%")
    percent_hispanic = "{:.2%}".format(df['latest.student.demographics.race_ethnicity.hispanic'][df[df['school.name'] == val].index[0]], "%")
    percent_asian = "{:.2%}".format(df['latest.student.demographics.race_ethnicity.asian'][df[df['school.name'] == val].index[0]], "%")
    acceptance_rate = "{:.2%}".format(df['latest.admissions.admission_rate.overall'][df[df['school.name'] == val].index[0]], "%")
    retention = "{:.2%}".format(df['latest.student.retention_rate.four_year.full_time'][df[df['school.name'] == val].index[0]])
    enrollment = int(df['latest.student.size'][df[df['school.name'] == val].index[0]])
    location = df['school.locale'][df[df['school.name'] == val].index[0]]
    in_state = "${:,.2f}".format(df['latest.cost.tuition.in_state'][df[df['school.name'] == val].index[0]])
    out_state = "${:,.2f}".format(df['latest.cost.tuition.out_of_state'][df[df['school.name'] == val].index[0]])
    grad_rate = "{:.2%}".format(df['latest.completion.completion_rate_4yr_100nt'][df[df['school.name'] == val].index[0]])
    salary_6 = "${:,.2f}".format(df['latest.earnings.6_yrs_after_entry.working_not_enrolled.mean_earnings'][df[df['school.name'] == val].index[0]])
    salary_8 = "${:,.2f}".format(df['latest.earnings.8_yrs_after_entry.mean_earnings'][df[df['school.name'] == val].index[0]])
    salary_10 = "${:,.2f}".format(df['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings'][df[df['school.name'] == val].index[0]])
    score = {"Average SAT": average_sat, "Average Math SAT": median_math_sat, "Average Verbal SAT": median_verbal_sat, "Average ACT": average_act,
             "Acceptance Rate": acceptance_rate, "Retention Rate": retention, "Undergraduate Enrollment": enrollment, "Location": location, 
             "Percent White": percent_white, "Percent Black": percent_black, "Percent Asian": percent_asian, "Percdent Hispanic": percent_hispanic,
             "In-state Tuition": in_state, "Out-of-state Tuition": out_state, "Graduation Rate": grad_rate, "Salary 6-years Post Entry": salary_6, 
             "Salary 8-years Post Entry": salary_8, "Salary 10-years Post-Entry": salary_10}
    return score

