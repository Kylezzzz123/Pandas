import pandas as pd

df = pd.read_csv('dogNames2.csv')

df[(800<df["Count_AnimalName"])&(df["Count_AnimalName"]<1000)]  # if multiple conditions, use &

pd.isnull(df)

a = df.iloc[:,0:1]
b = a.tail(10)
print(a)
print(b)

df['Count_AnimalName'].mean()
