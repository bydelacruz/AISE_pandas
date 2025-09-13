# How to manipulate textual data
import pandas as pd

titanic = pd.read_csv("titanic_data.csv")

# Convert the 'Name' column to lowercase
titanic["Name"].str.lower()


# lets create a new column 'Surname' that contains the surname of the passengers by extracting the part before the comma.
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)

# lets extract the passenger data about the countesses on board of the titanic
countess_data = titanic[titanic["Name"].str.contains("Countess")]

# lets find the passenger with the longest name
longest_name = titanic.loc[titanic["Name"].str.len().idxmax(), "Name"]

# in the Sex column lets replace the values of "male" with "M" and "female" with "F"
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
