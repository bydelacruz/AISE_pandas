# here we have examples of creating plots in pandas
# be sure to install matplotlib

import matplotlib.pyplot as plt
import pandas as pd

"""
below we first read our csv as usual.
but this time we used the index_col and parse_dates args.
this defines the  (0th) column as index of the resulting 
DataFrame and converts the dates in the column to Timestamp
onjects, respectively.
"""
air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

"""
here we can get a quick visual check of the data.
with a DataFrame, pandas creates by default one line plot for each
of the columns with numeric data.
"""

# air_quality.plot()

# plt.show()

"""
we can also just plot  only  the columns of the data table with 
specific data. example, lets just plot the data from paris
"""

# air_quality["station_paris"].plot()
# plt.show()

"""
we can also visually compare data. lets visually compare the NO2 values in london
versus paris
"""

# air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
# plt.show()

"""
there are several types of plots we can do. here is code that prints the various plots available
"""

"""
print(
[
    method_name
    for method_name in dir(air_quality.plot)
    if not method_name.startswith("_")
]
)
"""

"""
we can also plot each column in a seperate subplot
"""

# axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
# plt.show()

"""
we can further customize, extend or save the resulting plot
"""

fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentration.png")
plt.show()
