# here ill have examples of how we can create new columns
# derived from existing columns

import pandas as pd

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

"""
lets express the NO2 concentration of the station in London in mg/m3.
we can create a new column by using the [] and adding in the new column
name.
NOTE: these calculations are done element-wise, meaning all values in the given 
column get affected at once. no need to use a loop to iterate each row.
"""

# air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
# print(air_quality.head())

"""
next we will check the ratio of values in paris versus antwep and then save
the result in a new column.
"""

# air_quality["ratio_paris_antwerp"] = (
#  air_quality["station_paris"] / air_quality["station_antwerp"]
# )
# print(air_quality.head())


"""
now lets see how we can rename the data columns to the corresponsing station identifiers used by OpenAQ
"""

air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

print(air_quality_renamed.head())
