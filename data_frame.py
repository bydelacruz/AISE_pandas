import pandas as pd

"""
manually storing data in a table by using the DataFrame method
the DataFrame method takes a Dict as argument. each key represents a column.
the values of those keys are lists where each item represents a row.
"""

df = pd.DataFrame(
    {
        "Name": [
            "Braud, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

# print(df)

"""
 Each column in a DataFrame is called a series
 we can target individual series (or column) by using bracket notation
"""

# print(df["Age"])

"""
 you can also create a Series from scratch. like this:
"""
ages = pd.Series([22, 35, 58], name="Age")
# print(ages)

"""
there are methods we can call like max() to get max number
"""

# print(df["Age"].max())

"""
there are also methods to gather numerical data like count, mean, std, etc 
"""
# print(df.describe())
