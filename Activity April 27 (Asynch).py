Joshua Palaya
CAS-05-601A

Created on Monday Apr 29, 2024 2:45 PM

@author : JPalaya

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(42)
X = np.linspace(0, 10, 100)
true_slope = 2
true_intercept = 1
true_sigma = 1
Y = true_slope * X + true_intercept + np.random.normal(0, true_sigma, size=len(X))

# Perform simple linear regression using numpy
coefficients = np.polyfit(X, Y, 1)
slope, intercept = coefficients

# Plot the data and the regression line
plt.plot(X, Y, 'b.', label='Observed data')
plt.plot(X, slope * X + intercept, 'r-', label='Regression line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()

# Print the slope and intercept
print("Slope:", slope)
print("Intercept:", intercept)
