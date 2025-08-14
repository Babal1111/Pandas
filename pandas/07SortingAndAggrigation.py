

import pandas as pd

#soting data in a col
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Salary': [1000,2000,3000,7000]
}

df= pd.DataFrame(data)

df.sort_values(by='Age', inplace=True)
print(df)

df.sort_values(by='Salary', ascending=False,inplace=True)
print(df)

#sorting multiple cols
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Salary': [1000,2000,3000,7000]
}

df= pd.DataFrame(data)
df.sort_values(by=['Age','Salary'],ascending=[True,False],inplace=True)
print(df)