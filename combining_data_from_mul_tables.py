# combining data from multiple tables
import pandas as pd

air_quality_no2 = pd.read_csv("air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "paremeter", "value"]]

air_quality_pm25 = pd.read_csv("air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "paremeter", "value"]]

# Concatenating objects


# lets combine the measurements of NO2 and PM25, two tables with a similar structure, in a singlle table
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)

"""
The concat() function performs concatenation operations of multiple tables along one of the
axes (row-wise or column-wise). By default concatenation is along axis 0, so the resulting
table combines the rows of the input tables

NOTE: The axis argument will return in a number of pandas methods that can be applied along an axis.
A DataFrame has two corresponding axes: the first running vertically downwards across rows (axis 0),
and the second running horizontally across columns (axis 1). Most operations like concatenation or summary
statistics are by default across rows (axis 0), but can be applied across columns as well.
"""
