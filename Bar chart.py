# -------------------------------------------------------------
# Create the bar chart for the temperature variation
# -------------------------------------------------------------

# Import pyplot
import matplotlib.pyplot as plt

# Create a list of cities and temperatures
x_cities = ['NewYork', 'London', 'Dubai', 'New Delhi','Tokyo']
y_temp = [75,65,105,98,90]

# Change the chart labels
plt.title("Temperaure Variation")
plt.xlabel("Cities")
plt.ylabel("Temperature")

# Create the Bar chart
plt.bar(x_cities,y_temp)

# Show the Plot
plt.show()


