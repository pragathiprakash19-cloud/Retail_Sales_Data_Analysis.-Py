import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. SETUP: Create a sample retail dataset
data = {
    'Date': pd.to_datetime(['2025-01-01', '2025-01-02', '2025-02-01', '2025-02-15', '2025-03-01', '2025-03-10']),
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Home'],
    'Sales': [500, 150, 450, 300, 200, 350],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male']
}
df = pd.DataFrame(data)

# 2. INSPECTION: See the first few rows and data types
print("--- Dataset Overview ---")
print(df.head())
print(df.info())

# 3. ANALYSIS: Grouping data to find insights
# Total sales by category
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

# 4. VISUALIZATION: Making the data pretty
plt.figure(figsize=(10, 5))

# Plot 1: Sales by Category
plt.subplot(1, 2, 1) # 1 row, 2 columns, index 1
sns.barplot(data=category_sales, x='Category', y='Sales', palette='viridis')
plt.title('Sales by Category')

# Plot 2: Sales by Gender
plt.subplot(1, 2, 2) # 1 row, 2 columns, index 2
sns.boxplot(data=df, x='Gender', y='Sales')
plt.title('Spending Distribution by Gender')

plt.tight_layout()
plt.show()
# --- FINAL COMPLETION STEPS ---

# 1. Descriptive Stats (Requirement #2)
print("\n--- Sales Statistics ---")
print(df['Sales'].describe()) 

# 2. Time Series Plot (Requirement #3)
plt.figure(figsize=(8, 4))
sns.lineplot(data=df, x='Date', y='Sales', marker='o')
plt.title('Sales Trends Over Time')
plt.show()

# 3. Recommendations (Requirement #6)
print("\n--- Recommendations ---")
print("1. Focus marketing on Electronics as it is the top-performing category.")
print("2. Investigate why female spending has a wider range than male spending.")

# 5. DESCRIPTIVE STATISTICS (Proposal Req #2)
print("\n--- Key Sales Statistics ---")
print(df['Sales'].describe())
print(f"Most frequent sale (Mode): {df['Sales'].mode()[0]}")

# 6. TIME SERIES ANALYSIS (Proposal Req #3)
plt.figure(figsize=(8, 4))
sns.lineplot(data=df, x='Date', y='Sales', marker='o', color='red')
plt.title('Sales Trend Over Time')
plt.xticks(rotation=45)
plt.show()