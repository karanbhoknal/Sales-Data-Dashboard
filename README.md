# Sales-Data-Dashboard
# 📊 Sales Data Dashboard

This project is a simple data analytics dashboard built using **Pandas**, **Matplotlib**, and **Plotly**. It visualizes a sample sales dataset with charts showing sales trends, top products, and regional performance.

---

## 🚀 Features

- Summary statistics of the sales data
- Total sales by region (Matplotlib)
- Interactive sales over time line chart (Plotly)
- Top-selling products bar chart (Plotly)
- Clean, readable Python code with visualizations

---

## 🗂️ Project Structure

```
data_dashboard/
├── data/
│   └── sales_data.csv           # Sample sales dataset
├── dashboard.py                 # Main script with analysis and visualizations
├── requirements.txt             # Required Python libraries
└── README.md                    # Project documentation
```

---

## 📦 Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
pandas
matplotlib
plotly
```

---

## 📊 Sample Dataset (`sales_data.csv`)

A sample CSV file with the following fields:

- `Date`: Date of transaction
- `Region`: Sales region (North, South, East, West)
- `Product`: Product name (Product A, B, C)
- `Quantity`: Quantity sold
- `Unit_Price`: Price per unit
- `Total_Sales`: Total sales = Quantity × Unit Price

You can find the CSV in the `data/` folder.

---

## ▶️ How to Run

Run the Python script:

```bash
python dashboard.py
```

You will see:

- Printed summary statistics
- Matplotlib bar chart: **Total Sales by Region**
- Plotly line chart: **Total Sales Over Time**
- Plotly bar chart: **Top-Selling Products**

---

## 🧠 Future Enhancements (Optional)

- Add filters for region and date range
- Build a Streamlit web version
- Export dashboard to HTML or PDF
- Add more KPIs (avg. unit price, top customer, etc.)

---

## 📌 Author

Made with 💡 using Python, Pandas, Matplotlib, and Plotly.  
Feel free to modify and extend this project for your own use.
