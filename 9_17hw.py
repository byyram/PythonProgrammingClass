import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv', index_col=0)

print("DataFrame Head:")
print(df.head())

print("\nDataFrame Tail:")
print(df.tail())

print("\nDescriptive Statistics:")
print(df.describe())

df.hist()
plt.show()