import pandas as pd
import numpy as np

# 1. Load the CSV into a Pandas DataFrame
df = pd.read_csv("sales.csv")

print("Original Data:")
print(df)

# 2. Add a new column "Total" = Quantity * Price
df["Total"] = df["Quantity"] * df["Price"]
print("\nData with Total column:")
print(df)

# 3. Using NumPy to calculate statistics
total_sales = df["Total"].sum()
average_daily_sales = np.mean(df["Total"])   # daily because each row is one day
std_daily_sales = np.std(df["Total"], ddof=0)  # population std

print(f"\nTotal Sales: {total_sales}")
print(f"Average Daily Sales: {average_daily_sales}")
print(f"Standard Deviation of Daily Sales: {std_daily_sales}")

# 4. Find best-selling product based on total quantity
best_selling_product = df.groupby("Product")["Quantity"].sum().idxmax()
print(f"\nBest-selling product based on quantity: {best_selling_product}")
