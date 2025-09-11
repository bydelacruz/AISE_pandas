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

"""
we can check to see how pandas interpreted each of the 
columns data types by requesting the pandas dtypes
attribute. 'object' dtype is a string.
"""

# print(titanic.dtypes)

"""
just how we use read_* to read data to pandas, 
we can use to_* to store data. the to_excel() method 
stores the data as an excel file. in the following
example. the sheet_name is named passengers instead
of the default Sheet1. setting index=False prevents
the saving of row index labels in the spreadsheet
"""

"""
NOTE: pandas uses openpyxl to write a file to excel.
you need to install it if not installed
"""

# titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)


"""
we can then reload the excel file data to a DataFrame
"""

# titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
# print(titanic.head())

"""
the info() method provides technical information about a
dataFrame
"""

# print(titanic.info())

"""
heres a break down of the info() print above:

It is indeed a DataFrame.

There are 891 entries, i.e. 891 rows.

Each row has a row label (aka the index) with values ranging from 0 to 890.

The table has 12 columns. Most columns have a value for each of the rows (all 891 values are non-null). Some columns do have missing values and less than 891 non-null values.

The columns Name, Sex, Cabin and Embarked consists of textual data (strings, aka object). The other columns are numerical data with some of them whole numbers (aka integer) and others are real numbers (aka float).

The kind of data (characters, integers,…) in the different columns are summarized by listing the dtypes.

The approximate amount of RAM used to hold the DataFrame is provided as well.
"""
