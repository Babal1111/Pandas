import pandas as pd

#dictionary
data = {
    "Name" : ['Ram', 'sham'],
    "Age" : [25, 26],
    "Gender" : ['Male', 'Female'],             
}

#creating dataframe
df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv")
df.to_csv("output.csv",index = False) 
df.to_excel("output2.xlsx",index=False)