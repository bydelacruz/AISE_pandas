# how to select subsets and working with specific data
import pandas as pd

titanic = pd.read_csv("titanic_data.csv")

"""
to select say, just the age column of the titanic passengers
we do it with square brackets.
"""

# ages = titanic["Age"]

# print(ages.head())

"""
as a single column is selected it returns a pandas series.
"""

"""
calling the shape attribute on a series will return a tuple
with the number of rows and columns in the series.
"""

# titanic["Age"].shape


"""
to select multiple columns, use a list of column names within
the selection brackets.
"""
# age_sex = titanic[["Age", "Sex"]]
# print(age_sex)


"""
we can also filter specific rows from a DataFrame.
here we pull the passengers that are older than 35 years.
we do this by placing a conditional expression inside the 
selection brackets.
"""

# above_35 = titanic[titanic["Age"] > 35]
# print(above_35.head())


"""
like the conditional expression, isin() conditional returns a True
for each row the values are in the provided list.
we can place the condition inside the brackets like before.
here we look for passengers from cabin class 2 and 3.

NOTE: if using the or/and operator remember that it must be used
like this: | (or) & (and)
"""

# class_23 = titanic[titanic["Pclass"].isin([2, 3])]

# print(class_23.head())


"""
we can use the notna() conditional function to check if a value
is not null.
"""

# age_no_na = titanic[titanic["Age"].notna()]


"""
to select a subset of both rows and columns, we need to use the 
loc/iloc operators. when using, the part before the comma is 
the rows you want, and the part after is the columns you want.
here we get the names of passsengers over 35
"""

# adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# print(adult_names.head())

"""
if interested in certain rows and columns based on their 
position, we use the iloc operator. here we get rows 10 til 25
and columns 3 to 5
"""

# titanic.iloc[9:25, 2:5]

"""
we can also asign new values to cols and rows when using 
loc or iloc. example, here we assign the name anonymous to 
the first 3 elements of the fourth column
"""

# titanic.iloc[0:3, 3] = "anonymous"
