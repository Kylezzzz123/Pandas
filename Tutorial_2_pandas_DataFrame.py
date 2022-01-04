import pandas as pd
import numpy as np

# read csv file
df = pd.read_csv('dogNames2.csv')
print(df)

pd.DataFrame(np.arange(12).reshape(3,4))   #rows and columns, 2-D

pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"), columns=list('WXYZ'))  # index is rows, columns is columns

d1 = {"name": ["Bonnie", "Tracy"], "age": [20,31], "tel": [10086, 10010]}
pd.DataFrame(d1)

d2 = [{"Name": "Bonnie","age":32, "tel": 10010}, {"Name": "Tracy", "tel": 10000}, {"Name": "Ken", "age": 22}]
d2
pd.DataFrame(d2)

print('*'*100)
df
df.head() # show first 5 rows
df.tail() # show last 5 rows
df.info()   
df.describe() # show mean, std, min, 25%, 50%,75%, max
