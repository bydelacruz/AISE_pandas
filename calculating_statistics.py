# how to calculate basic statistics from pandas DataFrame
import pandas as pd

titanic = pd.read_csv("titanic_data.csv")

"""
we can do statistics aggregation with pandas as well.
lets show this by getting the average age of the titanic passengers.

there are different statistics available and can be applied to columns
with numerical data. Operations in general exclude missing data and operate
across rows by default.
"""
# here we get the mean of all ages
# titanic["Age"].mean()

# here we get the median age and ticket fare price of the titanic passengers
# titanic[["Age", "Fare"]].median()

"""
instead of the predefined statistics, specific combinations of aggregating
statistics for given columns can be defined using the DataFrame.agg() method
"""

"""
titanic.agg(
    {"Age": ["min", "max", "median", "skew"], "Fare": ["min", "max", "median", "mean"]}
)
"""

"""
we can aggregate statistics and group them by category
"""

# lets get the average age for male vs female titanic passsengers
# titanic[["Sex", "Age"]].groupby("Sex").mean()

# because the [] selection is also supported on the groupby method we can apply it like this
# titanic.groupby("Sex")["Age"].mean()

"""
we can get a toltal count using value_count() method.
"""

# lets get the number of passengers in each of the cabin classes
# titanic["Pclass"].value_count()
