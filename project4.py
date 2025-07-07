import numpy as np

monthly_sales = np.array([
    [100, 150, 200],
    [175, 225, 250],
    [300, 280, 320]
])

print(monthly_sales[:, 2])  # print third column of all rows

print(f"Monthly sales shape: {monthly_sales.shape}")
print(f"Size: {monthly_sales.size}")
print(f"Dimensions: {monthly_sales.ndim}")
print(f"Data type: {monthly_sales.dtype}")
