# how to rehshape a table layout to do things like sort columns, hide columns, and change column widths

import pandas as pd

titanic = pd.read_csv("titanic.csv")
air_quality = pd.read_csv("air_quality_no2.csv", index_col="date.utc", parse_dates=True)

# sorting


# lets sort the titanic data according to the age of the passengers
titanic_sorted_by_age = titanic.sort_values(by="Age")

# lets sort the titanic data according to the cabin class and age in descending order
titanic_sorted_by_class_and_age = titanic.sort_values(
    by=["Pclass", "Age"], ascending=False
)


# Long to wide format


"""
Let’s use a small subset of the air quality data set. We focus on
 data and only use the first two measurements of each location (i.e. the head of each group).
 The subset of data will be called no2_subset.
"""

# filter for no2 data only
no2 = air_quality[air_quality["parameter"] == "no2"]

# use 2 measurements per location
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# lets get the values for the three stations as seperate columns next to each other
no2_wide = no2_subset.pivot(columns="location", values="value")

"""
The pivot() function is purely reshaping of the data: a single value for each
index/column combination is required. As pandas supports plotting of multiple
columns (see plotting tutorial) out of the box, the conversion from long to wide
table format enables the plotting of the different time series at the same time
"""
no2.pivot(columns="location", values="value").plot()


# pivot table


# lets get the ean concentration for NO2 and PM2.5 in each of the stations in table form.
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
"""
In the case of pivot(), the data is only rearranged. When multiple values need to be aggregated
(in this specific case, the values on different time steps), pivot_table() can be used, providing
an aggregation function (e.g. mean) on how to combine these values. Pivot table is a well known
concept in spreadsheet software. When interested in the row/column margins
(subtotals) for each variable, set the margins parameter to True
"""


# wide to long format


# Starting from the wide format table created in the previous section,
# we add a new index to the DataFrame with reset_index()
no2_wide_reset = no2_wide.reset_index()

# now lets collect all the air quality NO2 measurements into a single column again
no_2 = no2_wide_reset.melt(id_vars="date.utc")

"""
The pandas.melt() method on a DataFrame converts the data table from wide format to long format.
The column headers become the variable names in a newly created column. The solution is the short
version on how to apply pandas.melt(). The method will melt all columns NOT mentioned in id_vars
together into two columns: A column with the column header names and a column with the values itself.
The latter column gets by default the name value.
The parameters passed to pandas.melt() can be defined in more detail:

The additional parameters have the following effects:
-value_vars defines which columns to melt together
-value_name provides a custom column name for the values column instead of the default column name value
-var_name provides a custom column name for the column collecting the column header names. Otherwise it
takes the index name or a default variable

Hence, the arguments value_name and var_name are just user-defined names for the two generated columns.
The columns to melt are defined by id_vars and value_vars.
"""
