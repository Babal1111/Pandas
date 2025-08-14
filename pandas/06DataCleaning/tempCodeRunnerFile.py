
data = {
    "Name": ["John", None, "Peter", "Linda"],
    "Age": [28, None, 35, 32],
    "Country": ["USA", None, "Australia", "Germany"],
    "City": ["New York", None, "Sydney", "Berlin"],
    "salary" :[10000,None,30000,259150]
}

df1 = pd.DataFrame(data)

print(df1['Age'].fillna(df['Age'].mean(),inplace=False))
