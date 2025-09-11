import pandas as pd

"""
use pandas to read the titanic data csv file.
we do that using the read_csv method of pandas
"""

titanic = pd.read_csv("titanic_data.csv")

"""
when displaying the dataFrame, the first 5 rows will be
shown by default
"""

# print(titanic)


"""
we can specify the number of rows we wish to see
by using the head() and passing in a number.
for example below we get the first 8 rows.

we can also use the tail() method to get the last N rows
"""

# print(titanic.head(8))
