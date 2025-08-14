import pandas as pd

data = {
    'Name': ['babal','preet','singh'],
    'age':[20,30,40],
    'marks':[90,80,70],
}

df = pd.DataFrame(data)
print(df)
#add a new col
df['bonus'] = df['marks'] * 10 #will be at end, we use this when we just want to add data, anywhere
print(df)

#using insert() insert at spesific pos
df.insert(3,"total Marks",[100,120,300])
print(df)

#updating SPECIFIC ROW DATA
df.loc[2,'marks'] = 2000
# here 2 is row index, andmarks col name
print(df)

#updating multiple vals, UPDAING WHOLE ROW
df['marks'] = df['marks']*2
#just like creating a new col


#deleting 
df.drop(columns='bonus',inplace=True)
#inplace=True means it will delete it from original df, false means it will reeturn new data frame
print(df)

#deleting multiple
df.drop(columns=['age','marks'],inplace=True)

print(df)