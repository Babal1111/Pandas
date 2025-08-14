import pandas as pd


data = {
    "Name": ["John", None, "Peter", "Linda"],
    "Age": [28, None, 35, 32],
    "Country": ["USA", None, "Australia", "Germany"],
    "City": ["New York", None, "Sydney", "Berlin"],
    "salary" :[10000,None,30000,259150]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull()) 
#will tell boolean of whole table where the vals are None

print(df.isnull().sum()) #will tell how many None values are in each column

df.dropna(axis= 0, inplace=True)
#dropna() function is used to drop rows or columns that contain missing values.
#axis=0 means we are dropping rows, axis=1 means we are dropping columns
print(df)

#--------------filling mising vals

data = {
    "Name": ["John", None, "Peter", "Linda"],
    "Age": [28, None, 35, 32],
    "Country": ["USA", None, "Australia", "Germany"],
    "City": ["New York", None, "Sydney", "Berlin"],
    "salary" :[10000,None,30000,259150]
}

df1 = pd.DataFrame(data)

df1.fillna(0,inplace=True)
#fillna() function is used to fill missing values with a specified value.
#here FIRST ARGUMENT is value
print(df1)


data = {
    "Name": ["John", None, "Peter", "Linda"],
    "Age": [28, None, 35, 32],
    "Country": ["USA", None, "Australia", "Germany"],
    "City": ["New York", None, "Sydney", "Berlin"],
    "salary" :[10000,None,30000,259150]
}

df = pd.DataFrame(data)

df['Age'].fillna(df['Age'].mean(),inplace=True)
#fillna() function is used to fill missing values with a specified value.
print(df)

