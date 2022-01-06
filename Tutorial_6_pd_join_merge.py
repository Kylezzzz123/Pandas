import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((2,4)), index=("A", "B"), columns=list("abcd"))
df1
df2 = pd.DataFrame(np.zeros((3,3)), index=("A", "B", "C"), columns=list("xyz"))
df2

df1.join(df2)
df2.join(df1)

df3 = pd.DataFrame(np.zeros((3,3)), columns=list("fax"))
df3
df1
df1.merge(df3,on="a")  # empty because df3 has no 1 and can't merge df1 
df3.loc[1,"a"] = 1   # replace zero to 1
df3
df1
df1.merge(df3,on="a")

df3 = pd.DataFrame(np.arange(9).reshape((3,3)), columns=list("fax"))
df3
df1
df1.merge(df3,on='a')   # combine the row with the same number in df3 and df1 

df4 = pd.DataFrame(np.arange(6).reshape((2,3)), index=("A","B"), columns=list("xyz"))
df4

df5 = pd.DataFrame(np.ones((2,4)), index=("C","D"), columns=list("komn"))
df5

df5.join(df4)
df4.join(df5)