
import pandas as pd

df = pd.read_csv("Balicontacts.csv",encoding="latin1")
print(df.head()) #no value thats 5 by default
print(df.head(10)) #first 10
print(df.tail(10)) #last 10

print(df.info())

data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "Country": ["USA", "UK", "Australia", "Germany"],
    "City": ["New York", "London", "Sydney", "Berlin"],
    "salary" :[10000,2000,30000,259150]
}

df = pd.DataFrame(data)
print(df)
print('discriptive stats')
print(df.describe())

df = pd.read_csv("Balicontacts.csv",encoding="latin1")
print('shape :')
print(df.shape)
print('colums: ')
print(df.columns)