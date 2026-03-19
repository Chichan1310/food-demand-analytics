import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Load the dataset
data = pd.read_csv("train.csv")

# 2️⃣ Graph 1: Total food orders per week
orders_per_week = data.groupby("week")["num_orders"].sum()

plt.figure()
orders_per_week.head(20).plot()
plt.title("Food Orders Per Week")
plt.xlabel("Week")
plt.ylabel("Orders")
plt.savefig("graph1_orders.png")  # saves the graph as an image

# 3️⃣ Graph 2: Top 10 meals ordered
meal_orders = data.groupby("meal_id")["num_orders"].sum().head(10)

plt.figure()
meal_orders.plot(kind="bar")
plt.title("Top Meals Ordered")
plt.xlabel("Meal ID")
plt.ylabel("Orders")
plt.savefig("graph2_meals.png")

# 4️⃣ Graph 3: Orders per fulfillment center
center_orders = data.groupby("center_id")["num_orders"].sum().head(10)

plt.figure()
center_orders.plot(kind="bar")
plt.title("Orders per Center")
plt.xlabel("Center ID")
plt.ylabel("Orders")
plt.savefig("graph3_centers.png")

print("Analytics finished")