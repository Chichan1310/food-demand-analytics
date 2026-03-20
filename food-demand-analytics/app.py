import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("output", exist_ok=True)

data = pd.read_csv("train.csv")

orders_per_week = data.groupby("week")["num_orders"].sum()

plt.figure()
orders_per_week.head(20).plot()
plt.title("Food Orders Per Week")
plt.xlabel("Week")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("output/graph1_orders.png")
plt.close()

meal_orders = data.groupby("meal_id")["num_orders"].sum().sort_values(ascending=False).head(10)

plt.figure()
meal_orders.plot(kind="bar")
plt.title("Top 10 Meals Ordered")
plt.xlabel("Meal ID")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("output/graph2_meals.png")
plt.close()

center_orders = data.groupby("center_id")["num_orders"].sum().sort_values(ascending=False).head(10)

plt.figure()
center_orders.plot(kind="bar")
plt.title("Orders per Fulfillment Center")
plt.xlabel("Center ID")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("output/graph3_centers.png")
plt.close()

print("👨‍🍳 Food demand analysis finished! Fresh graphs are waiting in the output/ folder.")
