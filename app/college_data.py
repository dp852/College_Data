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

'''
def data_request(val):
  print(val)
  median_math_sat = int(df['latest.admissions.sat_scores.midpoint.math'][df[df['school.name'] == val].index[0]])
  median_verbal_sat = int(df['latest.admissions.sat_scores.midpoint.critical_reading'][df[df['school.name'] == val].index[0]])
  lower_math = int(df['latest.admissions.sat_scores.25th_percentile.math'][df[df['school.name'] == val].index[0]])
  lower_verbal = int(df['latest.admissions.sat_scores.25th_percentile.critical_reading'][df[df['school.name'] == val].index[0]])
  upper_math = int(df['latest.admissions.sat_scores.75th_percentile.math'][df[df['school.name'] == val].index[0]])
  upper_verbal = int(df['latest.admissions.sat_scores.75th_percentile.critical_reading'][df[df['school.name'] == val].index[0]])
  median_act = int(df['latest.admissions.act_scores.midpoint.cumulative'][df[df['school.name'] == val].index[0]])
  lower_act = int(df['latest.admissions.act_scores.25th_percentile.cumulative'][df[df['school.name'] == val].index[0]])
  upper_act = int(df['latest.admissions.act_scores.75th_percentile.cumulative'][df[df['school.name'] == val].index[0]])
  percent_white = "{:.2%}".format(df['latest.student.demographics.race_ethnicity.white'][df[df['school.name'] == val].index[0]], "%")
  percent_black =  "{:.2%}".format(df['latest.student.demographics.race_ethnicity.black'][df[df['school.name'] == val].index[0]], "%")
  percent_hispanic = "{:.2%}".format(df['latest.student.demographics.race_ethnicity.hispanic'][df[df['school.name'] == val].index[0]], "%")
  percent_asian = "{:.2%}".format(df['latest.student.demographics.race_ethnicity.asian'][df[df['school.name'] == val].index[0]], "%")

'''

'''
if __name__== "__main__":
    print("Admissions Info:")
    if df['latest.admissions.admission_rate.overall'][df[df['school.name'] == val].index[0]] !=0:
        print("Acceptance rate:", "{:.2%}".format(df['latest.admissions.admission_rate.overall'][df[df['school.name'] == val].index[0]], "%"))
    else: 
        print("The college you selected did not report admissions rate")
    if df['latest.admissions.sat_scores.midpoint.critical_reading'][df[df['school.name'] == val].index[0]] != 0:
        print("Average SAT:", median_math_sat+median_verbal_sat, "range: ", lower_math+lower_verbal,"-",upper_math+upper_verbal)
        print("Average Math SAT:", median_math_sat, "range:",lower_math,"-",upper_math)
        print("Average Verbal SAT:", median_verbal_sat, "range:",lower_verbal,"-",upper_verbal)
    else: 
        print("The college you selected did not report SAT scores")
    if df['latest.admissions.act_scores.midpoint.cumulative'][df[df['school.name'] == val].index[0]] != 0:
        print("Average ACT:", median_act, "range:", lower_act, "-", upper_act)
    else: 
        print("The college you selected did not report ACT scores")
    print("Student Experience:")
    print("Retention rate:", "{:.2%}".format(df['latest.student.retention_rate.four_year.full_time'][df[df['school.name'] == val].index[0]]))
    print("Undergraduate Enrollment:", int(df['latest.student.size'][df[df['school.name'] == val].index[0]]), "students")
    print("Location:", df['school.locale'][df[df['school.name'] == val].index[0]])
    print("Student Demographics:", percent_white, "White,", percent_black, "Black,", percent_hispanic, "Hispanic,", percent_asian, "Asian")
    print("Tuition:", "In-State Tuition -", "${:,.2f}".format(df['latest.cost.tuition.in_state'][df[df['school.name'] == val].index[0]]), ",", "Out-Of-State Tuition-", "${:,.2f}".format(df['latest.cost.tuition.out_of_state'][df[df['school.name'] == val].index[0]]))
    print("Student Success:")
    print("4-year graduation rate:", "{:.2%}".format(df['latest.completion.completion_rate_4yr_100nt'][df[df['school.name'] == val].index[0]]))
    print("Average salary after 6 years of entry:", "${:,.2f}".format(df['latest.earnings.6_yrs_after_entry.working_not_enrolled.mean_earnings'][df[df['school.name'] == val].index[0]]))
    print("Average salary after 8 years of entry:", "${:,.2f}".format(df['latest.earnings.8_yrs_after_entry.mean_earnings'][df[df['school.name'] == val].index[0]]))
    print("Average salary after 10 years of entry:", "${:,.2f}".format(df['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings'][df[df['school.name'] == val].index[0]]))

'''