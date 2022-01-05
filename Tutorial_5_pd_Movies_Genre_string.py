import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv('Movies.csv')
df['Genre']

# caterite list  
temp_list = df["Genre"].str.split(",").tolist() # [[],[],[]]
genre_list = list(set([i for j in temp_list for i in j]))

zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))), columns=genre_list)  # df.shape[0] is give number of row count, df.shape[1] is give number of column count
print(zeros_df)

# give movies to classification position to 1
for i in range(df.shape[0]):     # for every row
    zeros_df.loc[i,temp_list[i]] = 1      # if the column has the genre in the row, put 1

# sum of the movies 
genre_count = zeros_df.sum(axis=0)     # axis=0 gives you total of each column in all rows,  axis=1 gives you total of each row in all columns
print(genre_count)

# sort
genre_count = genre_count.sort_values()
_x = genre_count.index
_y = genre_count.values
# plot
plt.figure(figsize=(20,8), dpi=80)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)),_x)
plt.show()
