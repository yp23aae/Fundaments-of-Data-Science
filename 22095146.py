import csv
import numpy as np
import matplotlib.pyplot as plt

# Read data from the CSV file
filename = 'data6.csv'
salaries = []

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        salaries.append(float(row[0]))

# Calculate the probability density function and plot the histogram
plt.hist(salaries, bins=30, density=True, alpha=0.75, color='blue', edgecolor='black',
         label='Empirical Probability Density Function')

# Calculate the mean annual salary (W~)
mean_salary = np.mean(salaries)

# Calculate the fraction of population with salaries between W~ and 1.25W~
lower_bound = mean_salary
upper_bound = 1.25 * mean_salary
fraction_between = np.sum((salaries >= lower_bound) & (salaries <= upper_bound)) / len(salaries)

# Calculate another value X
# This value represents the fraction of the population with salaries between W~ and 1.25W~
# The range is determined by the calculated lower and upper bounds
value_X = fraction_between

# Plot vertical lines for mean salary and 1.25 * mean salary
plt.axvline(mean_salary, color='red', linestyle='dashed', linewidth=2, label=f'Mean Salary (W~): {mean_salary:.2f}')
plt.axvline(upper_bound, color='green', linestyle='dashed', linewidth=2, label=f'1.25 * Mean Salary: {upper_bound:.2f}')

# Display legend, labels, and title
plt.legend()
plt.xlabel('Annual Salary (Euros)')
plt.ylabel('Probability Density')
plt.title('Empirical Probability Density Function of Annual Salaries')

# Print the calculated values on the graph
plt.text(mean_salary, 0.015, f'Mean Salary (W~): {mean_salary:.2f}', rotation=90, color='red')
plt.text(upper_bound, 0.015, f'1.25 * Mean Salary: {upper_bound:.2f}', rotation=90, color='green')
plt.text(upper_bound, 0.03, f'Fraction (W~ to 1.25W~): {fraction_between:.2%}', rotation=90, color='black')
plt.text(upper_bound, 0.045, f'Value X: {value_X:.2%}', rotation=90, color='black')

# Show the plot
plt.show()
