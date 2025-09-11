import pandas as pd

# manually storing data in a table by using the DataFrame method
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

print(df)

"""
the DataFrame method takes a Dict as argument. each key represents a column.
the values of those keys are lists where each item represents a row.
"""
