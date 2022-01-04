import pandas as pd
from matplotlib import pyplot as plt

file_path = "Movies.csv"
df = pd.read_csv(file_path)

df.head(1)
df.info()

# rating and runtime distribution
# choose plot

runtime_data = df["Runtime (Minutes)"].values

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

num_bin = (max_runtime - min_runtime)//5

# set size of plot
plt.figure(figsize=(20,8), dpi=80)
plt.hist(runtime_data, num_bin)

plt.xticks(range(min_runtime,max_runtime+5,5))
plt.show()
