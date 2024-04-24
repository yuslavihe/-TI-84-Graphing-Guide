import numpy as np
import matplotlib.pyplot as plt
import csv

# Function to generate polynomial coefficients
def generate_polynomial(points):
    n = len(points)
    X = np.array([p[0] for p in points])
    Y = np.array([p[1] for p in points])

    # Creating the Vandermonde matrix
    V = np.column_stack([X**i for i in range(n)])

    # Solving the system of linear equations to find polynomial coefficients
    coefficients = np.linalg.solve(V, Y)
    return coefficients

# Function to evaluate polynomial for given x
def evaluate_polynomial(coefficients, x):
    return sum(coef * x**i for i, coef in enumerate(coefficients))

# Convert coefficients to LaTeX format
def format_polynomial_latex(coefficients):
    terms = []
    for i in range(len(coefficients)):
        coef = coefficients[i]
        if i == 0:
            terms.append(f"{coef:.3f}")
        else:
            terms.append(f"{coef:.3f}x^{{{i}}}")
    return 'y & =' + ' + '.join(terms[::-1])

# Read points from file
points = []
with open('temp.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        points.append((x, y))

# Generating polynomial coefficients
coefficients = generate_polynomial(points)

# Displaying the polynomial
print(coefficients)
latex_polynomial = format_polynomial_latex(coefficients)
print("Polynomial in LaTeX format:", latex_polynomial)

# Generating points for the plot
x_values = np.linspace(min([p[0] for p in points]), max([p[0] for p in points]), 100)
y_values = [evaluate_polynomial(coefficients, x) for x in x_values]

# Plotting
plt.plot(x_values, y_values, label='$' + latex_polynomial + '$', color='blue')
plt.scatter(*zip(*points), label='Data points', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Interpolation')
plt.legend()
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt

# Define the range of x values
x_range = range(int(min(x_values)), int(max(x_values)) + 1)
x_coordinates = []
y_coordinates = []

# Iterate over the range of x values
for x in x_range:
    # Evaluate the polynomial at the current x value
    y = evaluate_polynomial(coefficients, x)
    # Append the current x and y coordinates to the lists
    x_coordinates.append(x)
    y_coordinates.append(y)

'''# Plot the graph
plt.figure()
plt.plot(x_values, y_values, label='$' + latex_polynomial + '$', color='blue')
plt.scatter(x_coordinates, y_coordinates, label='Interpolated points', color='green')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Interpolation with Interpolated Points')
plt.legend()
plt.grid(True)
plt.show()'''

# Write coordinates to CSV file
with open('coordinates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['X', 'Y'])  # Write header
    for x, y in zip(x_coordinates, y_coordinates):
        writer.writerow([round(x), round(y)])
