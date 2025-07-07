import numpy as np
quaterly_sales = np.array([
    [180, 150, 200],  
    [175, 225, 250],  
    [300, 280, 320],  
    [250, 270, 290] 
])
total_by_quarter = np.sum(quaterly_sales, axis=1) 
print(f"Total by quarter (row addition): {total_by_quarter}")

total_by_month = np.sum(quaterly_sales, axis=0) 
print(f"Total by month (column addition): {total_by_month}")


grand_total = np.sum(quaterly_sales) 
print(f"Grand total sales: {grand_total}")

avg_by_quarter = np.mean(quaterly_sales, axis=1)
print(f"Average by quarter: {avg_by_quarter}")

data = np.arange(12) 
print(f"Original data: {data}")

matrix_3x4 = data.reshape(3, 4)
print(f"3x4 matrix:\n{matrix_3x4}")

matrix_2x6 = data.reshape(2, 6)
print(f"2x6 matrix:\n{matrix_2x6}")

flattened_data = matrix_3x4.flatten()
print(f"Flattened data: {flattened_data}")

transposed_matrix = matrix_3x4.T
print(f"Transposed matrix:\n{transposed_matrix}")

q1_sales = np.array([100, 150, 200])
q2_sales = np.array([175, 225, 250])

horizontal_stack = np.hstack((q1_sales, q2_sales))
print(f"Horizontal stack: {horizontal_stack}")

vertical_stack = np.vstack((q1_sales, q2_sales))
print(f"Vertical stack:\n{vertical_stack}")

concatenated_sales = np.concatenate((q1_sales, q2_sales))
print(f"Concatenated sales: {concatenated_sales}")

year_data = np.array([100, 150, 200, 175, 225, 250, 300, 280, 320, 250, 270, 290])
quarters = np.split(year_data, 4)
print(f"Q1: {quarters[0]}")
print(f"Q2: {quarters[1]}")
print(f"Q3: {quarters[2]}") 
print(f"Q4: {quarters[3]}")


matrix = np.array([[4, 2], [1, 3]])

det = np.linalg.det(matrix)
print(f"Determinant: {det}")

try:
    inverse = np.linalg.inv(matrix)
    print(f"Inverse:\n{inverse}")
except np.linalg.LinAlgError as e:
    print(f"Error calculating inverse: {e} (Matrix might be singular)")

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

matrix_product = np.dot(A, B)
print(f"Matrix Product (A dot B):\n{matrix_product}")

element_wise_product = A * B
print(f"Element-wise product (A * B):\n{element_wise_product}")

