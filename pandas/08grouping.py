import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda','tinda'],
    'Age': [28, 24, 35, 32, 24],
    'Salary': [1000,2000,3000,7000,4000]
}

df= pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

grouped2 = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped2)