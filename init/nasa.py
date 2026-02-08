import matplotlib.pyplot as plt

# Define the points
x = [0, 2]
y = [0, 4]

# Create the plot
plt.plot(x, y, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Line from (0,0) to (2,4)')
plt.grid(True)
plt.show()
