import pandas as pd

CoDist = pd.read_csv("C:\\Users\\bayra\\OneDrive\\Desktop\\EEC3150\\CollegeDistance.csv")

first = CoDist.head(7)
last = CoDist.tail(7)

print(CoDist.head(7))
print(CoDist.tail(7))


data1 = pd.DataFrame(first)
data2 = pd.DataFrame(last)
#(DataFrame.column == 'value').describe()

print(data1.describe())
print(data2.describe())