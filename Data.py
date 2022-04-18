import requests
import pandas as pd

base_url = "https://api.data.gov/ed/collegescorecard/v1/"
dataset = "schools.json?"
filter_params = "school.degrees_awarded.predominant=3"
fields = ["id",
          "school.name",
          ".school.locale"
          "latest.student.size",
          "location.lat",
          #"location.lon",
          #"location.city",
          #"location.state",
          #"latest.admissions.admission_rate.overall",
          #"latest.admissions.sat_scores.midpoint.math",
          #"latest.admissions.sat_scores.25th_percentile.math",
          #"latest.admissions.sat_scores.75th_percentile.math",
          #"latest.admissions.sat_scores.midpoint.critical_reading",
          #"latest.admissions.sat_scores.25th_percentile.critical_reading",
          #"latest.admissions.sat_scores.75th_percentile.critical_reading",
          #"latest.admissions.act_scores.25th_percentile.cumulative",
          #"latest.admissions.act_scores.midpoint.cumulative",
          #"latest.admissions.act_scores.75th_percentile.cumulative",
          #"latest.completion.title_iv.depend.completed_by.4yrs"
          #"latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings"
          #"latest.earnings.10_yrs_after_entry.working_not_enrolled.std_dev"
          #"latest.earnings.6_yrs_after_entry.working_not_enrolled.mean_earnings"
          #"latest.earnings.6_yrs_after_entry.working_not_enrolled.std_dev"
          #"latest.earnings.8_yrs_after_entry.mean_earnings"
          #"latest.earnings.8_yrs_after_entry.std_deviation"
          #"latest.completion.completion_rate_4yr_100nt"




          "oops.variable.does.not.exist"]
options = "&per_page=100&page=0"
api_key = "&api_key=cZauPwdyxxKrzuVe7mM8WYOrWAQZymc9UsHhn3QV" 

request_url = base_url + dataset + filter_params + \
              "&fields=" + ",".join(fields) + options + api_key
print(request_url[:-40])