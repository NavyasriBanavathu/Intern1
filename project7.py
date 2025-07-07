import numpy as np
transactions = np.array([100, 150, 200, 3000, 250, 5000, 180, 220, 7000, 190, 120, 130, 4000, 170, 6000])
fraud_threshold = 1000

is_fraud = transactions > fraud_threshold

print("All Transactions: ", transactions)

print("Fraudulent Transactions (True = Fraud): ", is_fraud)

normal_transactions = transactions[~is_fraud]

avg_normal_amount = np.mean(normal_transactions)
print("Average Normal Transaction Amount: ", avg_normal_amount)

diff_from_avg = np.abs(transactions - avg_normal_amount)
print("Difference from Average: ", diff_from_avg)

secondary_threshold = 2000

high_diff = diff_from_avg > secondary_threshold
print("High Difference from Average (True = Suspicious): ", high_diff)

fraud_count = np.sum(is_fraud)
print("Number of Potential Fraud Cases: ", fraud_count)

max_transaction = np.max(transactions)
print("Maximum Transaction Amount: ", max_transaction)

min_transaction = np.min(transactions)
print("Minimum Transaction Amount: ", min_transaction)

std_dev = np.std(transactions)
print("Standard Deviation of Transactions: ", std_dev)

outlier_threshold = 2 * std_dev
is_outlier = diff_from_avg > outlier_threshold
print("Outliers (True = Beyond 2 Std Dev): ", is_outlier)

fraud_amounts = transactions[is_fraud]
total_fraud_amount = np.sum(fraud_amounts)
print("Total Amount of Potential Fraud Transactions: ", total_fraud_amount)

total_transactions = len(transactions)
fraud_percentage = (fraud_count / total_transactions) * 100
print("Percentage of Potential Fraud Transactions: ", fraud_percentage)

median_normal = np.median(normal_transactions)
print("Median of Normal Transactions: ", median_normal)