import pandas as pd

df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
    'Age': [25, 30, 35, 40, 45],
})

df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 9],
    'OrderID': [101, 102, 103, 104, 105],
})


df_merge = pd.merge(df_customers,df_orders,on="CustomerID", how="inner")
print("inner join")
print(df_merge)
#jinki keys math hori bs whi aye h

df_merge2 = pd.merge(df_customers,df_orders,on="CustomerID", how="outer")
print("outer join")
print(df_merge2)
#sari arey , or jo val match nhi hori woh NaN


df_merge3 = pd.merge(df_customers,df_orders,on="CustomerID", how="left")
print("left join")
print(df_merge3)
#sirrf left wala rkha ara, agr wor rigth m nhi to NaN


df_merge3 = pd.merge(df_customers,df_orders,on="CustomerID", how="right")
print("right join")
print(df_merge3)

df_merge3 = pd.merge(df_customers,df_orders,on="CustomerID", how="cross ")
print("Cross join")
print(df_merge3)

