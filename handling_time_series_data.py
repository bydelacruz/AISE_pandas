# how to handle time series data in Python using pandas and matplotlib
import pandas as pd

# Load the time series data
air_quality = pd.read_csv("air_quality_no2_long.csv")
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
