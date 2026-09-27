import pandas as pd
import matplotlib.pyplot as plt

# Load data

df = pd.read_csv(
    "data/sales_performance_cleaned.csv"
)

df["Date"] = pd.to_datetime(df["Date"])


# Create metrics

df["Revenue"] = df["Quantity"] * df["Unit_Price"]


# Overall metrics

total_revenue = df["Revenue"].sum()


# Category analysis

revenue_by_category = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

revenue_percentage_by_category = (
    revenue_by_category / total_revenue * 100
).round(2)

category_analysis = pd.DataFrame({
    "Revenue": revenue_by_category,
    "Revenue_Percentage": revenue_percentage_by_category
})

# Product analysis

revenue_by_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

quantity_by_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

average_price_by_product = (
    revenue_by_product / quantity_by_product
).round(2)

revenue_percentage_by_product = (
    revenue_by_product / total_revenue * 100
).round(2)


# Region analysis


revenue_by_region = (
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)


# Channel analysis

revenue_by_channel = (
    df.groupby("Channel")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

revenue_percentage_by_channel = (
    revenue_by_channel / total_revenue * 100
).round(2)


# Time analysis

revenue_by_date = (
    df.groupby("Date")["Revenue"]
    .sum()
    .sort_index()
)

df["Month"] = df["Date"].dt.month

revenue_by_month = (
    df.groupby("Month")["Revenue"]
    .sum()
    .sort_index()
)

best_month = revenue_by_month.idxmax()
best_month_revenue = revenue_by_month.max()

worst_month = revenue_by_month.idxmin()
worst_month_revenue = revenue_by_month.min()



# Output

print("\n========== OVERALL ==========")

print("Total Revenue:", total_revenue)


print("\n========== CATEGORY ==========")

print(category_analysis)


print("\n========== PRODUCT ==========")

print("Revenue:")
print(revenue_by_product)

print("\nQuantity:")
print(quantity_by_product)

print("\nAverage Price:")
print(average_price_by_product)

print("\nRevenue Percentage:")
print(revenue_percentage_by_product)


print("\n========== REGION ==========")

print(revenue_by_region)


print("\n========== CHANNEL ==========")

print("Revenue:")
print(revenue_by_channel)

print("\nPercentage:")
print(revenue_percentage_by_channel)


print("\n========== MONTH ==========")

print("\n")

print("\nHighest Revenue Month:")
print("Month:", best_month)
print("Revenue:", best_month_revenue)

print("\nLowest Revenue Month:")
print("Month:", worst_month)
print("Revenue:", worst_month_revenue)

print("\nDifference:")
print(best_month_revenue - worst_month_revenue)

# Monthly Revenue Chart

plt.figure()

month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September"
]

plt.plot(
    revenue_by_month.index, 
    revenue_by_month.values,
    marker="o"
)

plt.title("Monthly Revenue Performance")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(
    revenue_by_month.index,
    month_names
)

plt.grid(True)

for month, revenue in zip(
    revenue_by_month.index, 
    revenue_by_month.values
):
    plt.annotate(
        f"{revenue:,.0f}",
        (month, revenue), 
        textcoords="offset points",
        xytext=(0,8),
        ha="center"
    )

plt.savefig("images/monthly_revenue.png")

plt.show()

# Revenue by Category Chart

plt.figure()

plt.bar(
    revenue_by_category.index,
    revenue_by_category.values
)

for category, revenue in zip(
    revenue_by_category.index,
    revenue_by_category.values
):
    plt.annotate(
        f"{revenue:,.0f}",
        (category, revenue),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center"
    )

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.savefig("images/revenue_by_category.png")

plt.show()

# Quantity by Product Chart

plt.figure()

plt.bar(
    quantity_by_product.index,
    quantity_by_product.values
)

for product, quantity in zip(
    quantity_by_product.index,
    quantity_by_product.values
):
    plt.annotate(
        f"{quantity:,.0f}",
        (product, quantity),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center"
    )

plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity")

plt.savefig("images/quantity_by_product.png")

plt.show()

# Revenue by Channel chart

plt.figure()

plt.bar(
    revenue_by_channel.index,
    revenue_by_channel.values
)

for channel, revenue in zip(
    revenue_by_channel.index,
    revenue_by_channel.values
):
    plt.annotate(
        f"{revenue:,.0f}",
        (channel, revenue),
        textcoords="offset points",
        xytext=(0,5),
        ha="center"
    )

plt.title("Revenue by Channel")
plt.xlabel("Channel")
plt.ylabel("Revenue")


plt.savefig("images/revenue_by_channel.png")

plt.show()

# Revenue by Region Chart

plt.figure()

plt.bar(
    revenue_by_region.index,
    revenue_by_region.values
)

for region, revenue in zip(
    revenue_by_region.index,
    revenue_by_region.values
):
    plt.annotate(
        f"{revenue:,.0f}",
        (region, revenue),
        textcoords="offset points",
        xytext=(0,5),
        ha="center"
    )

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.savefig("images/revenue_by_region.png")

plt.show()