# 🍽️ Food Demand Analytics – Docker Guide

This project analyzes food demand data and generates graphs that visualize ordering trends.
The graphs are automatically saved in the **output/** folder after running the Docker container.

---

# 🐳 Running the Project Using Docker

Follow the steps below to run the project.

---

## 1️⃣ Open the Project in VS Code

1. Open **Visual Studio Code**.
2. Click **File → Open Folder**.
3. Select the project folder:

food-demand-analytics

---

## 2️⃣ Open the Terminal in VS Code

Open the built-in terminal using one of the following methods:

**Option 1 (Shortcut):**
Press:

Ctrl + `

**Option 2 (Menu):**

Terminal → New Terminal

Make sure the terminal path shows the **food-demand-analytics** folder.

---

## 3️⃣ Build the Docker Image

In the terminal, type the following command:

docker build -t food-demand-analytics .

This command builds the Docker image for the analytics project.

---

## 4️⃣ Run the Docker Container

Run the container with this command:

docker run --name christian-food-demand -v "${PWD}/output:/app/output" food-demand-analytics

This command will:

• Run the analytics script
• Generate data visualization graphs
• Save the graphs inside the **output/** folder

---

## 5️⃣ View the Generated Graphs

After the container finishes running, open the folder:

output/

You should see the generated graphs:

graph1_orders.png
graph2_meals.png
graph3_centers.png

---

# 📊 Expected Output

If the container runs successfully, the Docker log will display:

👨‍🍳 Food demand analysis finished!
Graphs successfully generated in the output/ folder.

---

# 👨‍💻 Author

Christian – Food Demand Analytics Project
