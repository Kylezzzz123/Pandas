import pandas as pd
import numpy as np

t3 = pd.DataFrame(np.arange(12).reshape(3,4), index=list('abc'), columns=list('WXYZ'))
t3
t3.loc["a","Z"]     # loc is to get data by labels
t3.loc['a']
t3.loc["a",:]
t3.loc[:,"Y"]
t3.loc[["a","c"]]
t3.loc[:,["W", "Z"]]

print('*'*100)
t3
t3.iloc[1]    # iloc is to get data by location
t3.iloc[:,2]
t3.iloc[:, [2,1]]
t3.iloc[[0,2],[2,1]]
t3.iloc[1:,:2] 
print('*'*100)
t3
t3.iloc[1:,:2] = 30   # replace numbers in that location to 30
t3