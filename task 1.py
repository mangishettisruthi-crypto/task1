Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# ======================================
# DATA IMMERSION & DATA WRANGLING PROJECT
# ======================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------
# STEP 1: Create Sample Dataset
# --------------------------------------

data = {
    'Order_ID': [101, 102, 103, 104, 104, 105],
    'Customer': ['Ravi', 'Sita', 'Ram', 'Kumar', 'Kumar', 'Priya'],
    'Product': ['Rice', 'Milk', 'Bread', 'Eggs', 'Eggs', 'Sugar'],
    'Quantity': [2, 1, np.nan, 5, 5, 3],
    'Price': [1200, 50, 40, np.nan, np.nan, 150]
}

df = pd.DataFrame(data)

print("=" * 50)
print("ORIGINAL DATASET")
print("=" * 50)
print(df)

# --------------------------------------
# STEP 2: DATA IMMERSION
# --------------------------------------

print("\n\nDATA IMMERSION")
print("=" * 50)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

# --------------------------------------
# STEP 3: DATA WRANGLING
# --------------------------------------

print("\n\nDATA WRANGLING")
print("=" * 50)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing Quantity
... df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
... 
... # Fill missing Price
... df['Price'] = df['Price'].fillna(df['Price'].mean())
... 
... # Convert datatype
... df['Quantity'] = df['Quantity'].astype(int)
... 
... # Create Total Sales column
... df['Total_Sales'] = df['Quantity'] * df['Price']
... 
... print("\nCleaned Dataset:")
... print(df)
... 
... # --------------------------------------
... # STEP 4: BASIC ANALYSIS
... # --------------------------------------
... 
... print("\n\nBASIC ANALYSIS")
... print("=" * 50)
... 
... total_revenue = df['Total_Sales'].sum()
... print("Total Revenue:", total_revenue)
... 
... best_product = df.groupby('Product')['Total_Sales'].sum()
... print("\nSales by Product:")
... print(best_product)
... 
... # --------------------------------------
... # STEP 5: VISUALIZATION
... # --------------------------------------
... 
... best_product.plot(kind='bar')
... 
... plt.title("Sales by Product")
... plt.xlabel("Product")
... plt.ylabel("Total Sales")
... plt.tight_layout()
... plt.show()
... 
... # --------------------------------------
... # STEP 6: SAVE CLEANED DATA
... # --------------------------------------
... 
... df.to_csv("Cleaned_Sales_Data.csv", index=False)
... 
