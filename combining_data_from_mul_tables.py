# combining data from multiple tables
import pandas as pd

air_quality_no2 = pd.read_csv("air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "paremeter", "value"]]

air_quality_pm25 = pd.read_csv("air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "paremeter", "value"]]
