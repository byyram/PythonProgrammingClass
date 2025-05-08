import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

diabetes = load_diabetes(as_frame=True)
df = diabetes.frame

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

plt.figure(figsize = (10, 6))
plt.scatter(X_test['bmi'], y_test, color='green')
plt.scatter(X_test['bmi'], y_pred, color='blue')
plt.xlabel('BMI')
plt.ylabel('Disease')
plt.legend()
plt.grid(True)
plt.show()
