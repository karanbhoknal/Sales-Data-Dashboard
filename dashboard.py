import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load CSV
df = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

# --- BASIC STATS ---
print("Summary Statistics:")
print(df.describe())

# --- AGGREGATED METRICS ---

# Total Sales by Region
region_sales = df.groupby("Region")["Total_Sales"].sum().reset_index()

# Total Sales Over Time
time_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()

# Top-Selling Products
top_products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).reset_index()

# --- MATPLOTLIB CHART: Bar Chart for Region Sales ---
plt.figure(figsize=(8, 5))
plt.bar(region_sales['Region'], region_sales['Total_Sales'], color='skyblue')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()

# --- PLOTLY CHARTS ---

# Sales over Time (Line Chart)
fig1 = px.line(time_sales, x='Date', y='Total_Sales', title='Total Sales Over Time')

# Top Products (Bar Chart)
fig2 = px.bar(top_products, x='Product', y='Total_Sales', title='Top-Selling Products')

# Show interactive charts
fig1.show()
fig2.show()
