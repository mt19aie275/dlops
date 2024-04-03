import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))
# Define the range of x-values
x = np.linspace(-3.5, 4.6, 100)  # 100 points between -3.5 and 4.6
# Calculate the sigmoid values
y = sigmoid(x)
# Plot the graph
plt.plot(x, y)
# Add labels and title
plt.xlabel("x")
plt.ylabel("sigmoid(x)")
plt.title("Sigmoid Function")
# Set limits slightly bigger than range of function
plt.xlim([-11, 11])
plt.ylim([-0.1, 1.1])
# Grid
plt.grid(True)
# Show the plot
plt.show()