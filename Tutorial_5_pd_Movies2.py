import pandas as pd
import numpy as np
df = pd.read_csv('Movies.csv')
df
df.info()

df.iloc[:,[5,8]]

# get average of rating

df["Rating"].mean()

# get number of directors
dir = df["Director"].tolist()
len(set(dir))    # set is to remove the duplicate directors
print(df["Director"].unique())

# get actors numbers

temp_actors_list = df["Actors"].str.split(", ").tolist()
print(temp_actors_list)

actors_list = [i for j in temp_actors_list for i in j]   # to remove duplicate in list
#actors_list = np.array(temp_actors_list).flatten()   # to split items in list
actors_sum = len(set(actors_list))
print(actors_sum) 