# how to handle time series data in Python using pandas and matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Load the time series data
air_quality = pd.read_csv("air_quality_no2_long.csv")
air_quality = air_quality.rename(columns={"date.utc": "datetime"})

# using pandas datetime properties


# lets convert the datetime column to a pandas datetime object
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])

"""
Initially, the values in datetime are character strings and do not provide
any datetime operations (e.g. extract the year, day of the week,…).
By applying the to_datetime function, pandas interprets the strings and
convert these to datetime (i.e. datetime64[ns, UTC]) objects. In pandas we
call these datetime objects similar to datetime.datetime from the standard
library as pandas.Timestamp.

NOTE: As many data sets do contain datetime information in one of the columns,
pandas input function like pandas.read_csv() and pandas.read_json() can do the
transformation to dates when reading the data using the parse_dates parameter
with a list of the columns to read as Timestamp:

pd.read_csv("data.csv", parse_dates=["datetime"])
"""


# Now we can use the datetime properties to extract information from the datetime column
# lets get the start and end date of the time series data set we are working with
start_end_dates = air_quality["datetime"].min(), air_quality["datetime"].max()

# using pandas.Timestamp for datetimes enables us to calculate with date information
# lets calculate the length of the time series
time_series_length = air_quality["datetime"].max() - air_quality["datetime"].min()

# lets now add a new column to the DataFrame containing only the month of the measurement
air_quality["month"] = air_quality["datetime"].dt.month

"""
By using Timestamp objects for dates, a lot of time-related properties are provided
by pandas. For example the month, but also year, quarter,… All of these properties
are accessible by the dt accessor.
"""

# lets find the average NO2 concentration for each day of the week for each measurement location
air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()

"""
Remember the split-apply-combine pattern provided by groupby from the tutorial on statistics
calculation? Here, we want to calculate a given statistic (e.g. mean) for each
weekday and for each measurement location. To group on weekdays, we use the datetime
property weekday (with Monday=0 and Sunday=6) of pandas Timestamp, which is also
accessible by the dt accessor. The grouping on both locations and weekdays can be
done to split the calculation of the mean on each of these combinations.
"""

# now lets plot the typical NO2 pattern during the day of our time series
# of all stations together. in oother words, what is the average value for eeach hour of the day

fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(
    kind="bar", rot=0, ax=axs
)
plt.xlabel("Hour of the day")  # customize the x-axis label
plt.ylabel("$NO_2 (µg/m^3)$)")  # customize the y-axis label
plt.title("Typical daily $NO_2$ pattern")  # add a title to the plot
plt.tight_layout()  # adjust the plot to make sure everything fits without overlapping

# uncomment the line below to display the plot
# plt.show()


# Datetime as index

"""
In the tutorial on reshaping, pivot() was introduced to reshape the data
table with each of the measurements locations as a separate column:
"""
no_2 = air_quality.pivot(index="datetime", columns="location", values="value")

"""
Working with a datetime index (i.e. DatetimeIndex) provides powerful
functionalities. For example, we do not need the dt accessor to get the
time series properties, but have these properties available on the index
directly:
"""
year_weekday = no_2.index.year, no_2.index.weekday


# lets create a plot of the NO2 values in the different stations from the 20th of
# May till the end of the 21st of May

no_2["2019-05-20":"2019-05-21"].plot()
# plt.show()


# Resample a time series to another frequency

# lets aggregate the current hourly time series values to the monthly
# maximum value in each of the stations

monthly_max = no_2.resample("ME").max()

"""
A very powerful method on time series data with a datetime index, is
the ability to resample() time series to another frequency
(e.g., converting secondly data into 5-minutely data).
The resample() method is similar to a groupby operation:
it provides a time-based grouping, by using a string (e.g. M, 5H,…)
that defines the target frequency it requires an aggregation function such as mean, max,…
"""
# when defined, the frequency of the time series is provided by the freq attribute:
frequency = monthly_max.index.freq

# lets plot the daily mean NO2 value in each of the stations
no_2.resample("D").mean().plot(style="-o", figsize=(10, 5))
