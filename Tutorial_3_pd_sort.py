import pandas as pd
import numpy as np
# read csv file
df = pd.read_csv('dogNames2.csv')
df.head()
df.info()

# DataFrame sort 
df = df.sort_values(by="Count_AnimalName", ascending=True)
df.tail(10)
df.head(10)
print('*'*100)

df[:20]  # first 20 rows
print('*'*100)
df[:20]["Row_Labels"]   # first 20 rows in the Row_Labels
df["Row_Labels"]
print('*'*100)

t3 = pd.DataFrame(np.arange(12).reshape(3,4), index=list('abc'), columns=list('WXYZ'))
t3
t3.loc["a","Z"]
t3.loc['a']
t3.loc["a",:]
t3.loc[:,"Y"]
t3.loc[["a","c"]]
t3.loc[:,["W", "Z"]]