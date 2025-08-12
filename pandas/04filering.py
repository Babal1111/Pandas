
import pandas as pd
 
 
df = pd.read_csv("Balicontacts.csv",encoding="latin1")

column = df['First Name']
print(column)
print(df.columns)
columns = df[["First Name","Last Name"]]
print(columns)

#-----------

data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "Country": ["USA", "UK", "Australia", "Germany"],
    "City": ["New York", "London", "Sydney", "Berlin"],
    "salary" :[10000,2000,30000,259150]
}

df = pd.DataFrame(data)
 
filterd_rows = df[(df["Age"]>30) ]
print(filterd_rows)

filtered = df[(df["Age"]>30) & (df["salary"] > 30000)]
print(filtered)

filtered = df[(df["Age"]>30) | (df["salary"] > 10000)]
print(filtered)