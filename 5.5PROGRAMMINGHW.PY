import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("C:/Users/bayra/OneDrive/Desktop/EEC3150/data.csv")
years = df['DATE'].values
temps = df['VALUE'].values
print(df.columns)

slope, intercept, r_value, p_value, std_err = stats.linregress(years, temps)

print(f"Simple Linear Regression Equation: Temperature = {slope:.4f} * Year + {intercept:.4f}")
print(f"R-squared Value: {r_value**2:.4f}")

plt.figure(figsize=(12, 6))
plt.scatter(years, temps)
plt.plot(years, slope * years + intercept, color = 'red')
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.title('Average Temperature in New York City 1987-2025')
plt.legend()
plt.grid(True)
plt.show()