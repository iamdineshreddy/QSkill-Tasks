import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("digital_payments_indian_banks.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

# Average Calculations
print("\nAverage UPI Transactions (Million):", df["UPI_Transactions_Million"].mean())
print("Average IMPS Transactions (Million):", df["IMPS_Transactions_Million"].mean())
print("Average NetBanking Users (Lakh):", df["NetBanking_Users_Lakh"].mean())
print("Average Total Revenue (Cr):", df["Total_Revenue_Cr"].mean())

# =======================================
# Bar Chart - UPI Transactions by Month
# =======================================
plt.figure(figsize=(12,5))
plt.bar(df["Month"], df["UPI_Transactions_Million"])
plt.title("Monthly UPI Transactions (in Millions)")
plt.xlabel("Month")
plt.ylabel("UPI Transactions (Million)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =======================================
# Scatter Plot - NetBanking Users vs Revenue
# =======================================
plt.figure(figsize=(7,5))
plt.scatter(df["NetBanking_Users_Lakh"], df["Total_Revenue_Cr"])
plt.title("NetBanking Users vs Total Revenue")
plt.xlabel("NetBanking Users (Lakh)")
plt.ylabel("Revenue (Cr)")
plt.grid(True)
plt.tight_layout()
plt.show()

# =======================================
# Heatmap - Correlation Matrix
# =======================================
plt.figure(figsize=(8,6))
numeric_df = df.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Digital Payments Dataset")
plt.tight_layout()
plt.show()
