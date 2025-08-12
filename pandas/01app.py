import pandas as pd

#reading from csv

import pandas as pd

df = pd.read_csv("Balicontacts.csv", encoding='latin1')
# print(df)

df2 = pd.read_json("babal.json")
print(df2)