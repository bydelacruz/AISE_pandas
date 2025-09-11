# how to select subsets and working with specific data
import pandas as pd

titanic = pd.read_csv("titanic_data.csv")

"""
to select say, just the age column of the titanic passengers
we do it with square brackets.
"""

# ages = titanic["Age"]

# print(ages.head())
