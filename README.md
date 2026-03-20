Open the Terminal in VS Code

Press:

Ctrl + `

or go to:

Terminal → New Terminal

Make sure you are inside the project folder.

 Build the Docker Image

Type this command in the terminal:

docker build -t food-demand-analytics .

This will create the Docker image for the analytics project.

Run the Docker Container

Run this command:

docker run --name christian-food-demand -v "${PWD}/output:/app/output" food-demand-analytics

This command will:

Run the analytics script

Generate graphs

Save the graphs in the output/ folder

Check the Generated Graphs

After running the container, open the folder:

output/

You should see the generated graphs:

graph1_orders.png
graph2_meals.png
graph3_centers.png
