
import pandas as pd

#interpolation meansfilling estimated vals in place of missing values

#it is based on mathematicla algos, linear etc

#linear interpolation
data = {
    "Time" :[1,2,3,4,5],
    "Value" : [10,None,30,None,50],
}

df = pd.DataFrame(data)
print(df)
df["Value"] =df["Value"].interpolate(method='linear')
print(df)


#polynomial interpolation
data = {
    "Time" :[1,2,3,4,5],
    "Value" : [10,None,30,None,50],
}

df = pd.DataFrame(data)

df["Value"] = df["Value"].interpolate(method='polynomial', order=2)  # quadratic
#order=2 → quadratic polynomial (you can try 3 for cubic, etc.).
print("\nAfter Polynomial Interpolation:\n", df)