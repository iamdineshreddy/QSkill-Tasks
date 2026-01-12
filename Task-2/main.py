import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv("house_prices.csv")
print(df.head())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Features & Target
X = df[["Rooms", "Size_sqft", "Location", "Age"]]
y = df["Price"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print("\nPredicted Prices:", y_pred)
print("Actual Prices:", y_test.values)

# Model Evaluation
print("\nMean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# ===========================
# Visualization
# ===========================

# Scatter: Actual vs Predicted
plt.figure(figsize=(7,5))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price (Lakhs)")
plt.ylabel("Predicted Price (Lakhs)")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.show()

# Feature importance (Coefficients)
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print("\nFeature Influence / Coefficients:")
print(coefficients)
