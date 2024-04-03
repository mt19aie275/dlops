def tanh(x):
  return np.sinh(x) / np.cosh(x)# Define the range of x-values
x = np.linspace(-5, 5, 1000)  # 1000 points between -5 and 5# Calculate tanh values
y = tanh(x)# Plot the graph
plt.plot(x, y)# Add labels and title
plt.xlabel("x")
plt.ylabel("tanh(x)")
plt.title("Tanh Function")# Set limits slightly bigger than range of function
plt.xlim([-5.5, 5.5])
plt.ylim([-1.1, 1.1])# Grid
plt.grid(True)# Show the plot
plt.show()