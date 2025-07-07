import numpy as np

sales_data = np.array([100, 150, 200, 175, 300])
print("Sales data: ", sales_data)
print("Type of sales_data: ", type(sales_data))
print(sales_data[-1])

monthly_sales = np.array([
    [199, 150, 200],
    [175, 225, 250],
    [300, 280, 320]
])
print(monthly_sales[:, -1])

print("Monthly sales shape: ", monthly_sales.shape)
print("Size: ", monthly_sales.size)
print("Dimensions: ", monthly_sales.ndim)
print("Data type: ", monthly_sales.dtype)

zeros_array = np.zeros(5)
one_array = np.ones((3, 4))
range_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)

print("Zeros: ", zeros_array)
print("Ones: ", one_array)
print("Range: ", range_array)
print("Linspace: ", linspace_array)

sales = np.array([100, 150, 200, 175, 300])
high_sales = sales > 180
print(f"High sales mask: {high_sales}")
high_sales_values = sales[high_sales]
print(f"High sales values: {high_sales_values}")

premium_sales = sales[sales > 200]
print(f"Premium sales: {premium_sales}")


prices = np.array([10, 15, 20, 25])
quantities = np.array([5, 3, 8, 2])
revenue = prices * quantities
print(f"Revenue: {revenue}")

discounted_prices = prices * 0.9
tax_included = prices * 1.1

price_difference = prices - np.mean(prices)
print(f"Discounted: {discounted_prices}")

prices = np.array([10, 15, 20, 25])

price_difference = prices - np.mean(prices)
print(f"Price difference from mean: {price_difference}") 

tax_included = prices * 1.1
print(f"With tax: {tax_included}")

sales_matrix = np.array([
    [100, 150, 200],
    [175, 225, 250],
    [300, 280, 320]
])

discounted = sales_matrix * 0.9
print(f"Discounted sales matrix: {discounted}")

monthly_bonus = np.array([10, 20, 15])

total_with_bonus = sales_matrix + monthly_bonus
print(f"Sales with total including bonus: {total_with_bonus}")


data = np.array([1, 4, 9, 16, 25])

sqrt_data = np.sqrt(data)
print(f"Square root of data: {sqrt_data}")

log_data = np.log(data)
print(f"Natural logarithm of data: {log_data}")

exp_data = np.exp(data)
print(f"Exponential of data: {exp_data}")

data = np.array([1, 4, 9, 16, 25])

sqrt_data = np.sqrt(data)
print(f"Square root: {sqrt_data}")

log_data = np.log(data)
print(f"Natural log: {log_data}")

exp_data = np.exp(data)
print(f"Exponential: {exp_data}")

angles = np.array([0, np.pi/2, np.pi, np.pi*1.5, np.pi*2]) 
sin_values = np.sin(angles)
print(f"Sine values: {sin_values}")

cos_values = np.cos(angles)
print(f"Cosine values: {cos_values}")

tan_values = np.tan(angles)
print(f"Tangent values: {tan_values}")

sales_data = np.array([100, 150, 250, 175, 300, 180, 220])

mean_sales = np.mean(sales_data)
print(f"Mean sales: {mean_sales}")

median_sales = np.median(sales_data)
print(f"Median sales: {median_sales}")

min_sales = np.min(sales_data)
print(f"Minimum sales: {min_sales}")

max_sales = np.max(sales_data)
print(f"Maximum sales: {max_sales}")

std_dev_sales = np.std(sales_data)
print(f"Standard deviation of sales: {std_dev_sales}")

variance_sales = np.var(sales_data)
print(f"Variance of sales: {variance_sales}")
