import pandas as pd
import numpy as np

t = pd.Series([1,2,31,12,3,4])
t
t[t>10]
print('*'*100)
t2 = pd.Series([1,23,2,2,1], index=list('abcde'))
t2
t2.astype(float)
print('*'*100)
temp_dict = {"name":"Bonnie", "age": 20, "tel":10086}
t3 = pd.Series(temp_dict)
t3
t3['age']
t3[1]
t3[:2]
t3[1:2]
t3.index
for i in t3.index:
    print(i)
len(t3.index)
list(t3.index)
list(t3.index)[:2]
print('*'*100)

