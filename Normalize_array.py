# This code noralizes array to be in the range of 0 1nd 1
import numpy as np

def normalize_array(arr):
    """
    Normalizes a NumPy array by scaling its values between 0 and 1 using min-max normalization.
    This ensures that the minimum value in the array becomes 0 and the maximum value becomes 1.
    """
    min_value = np.min(arr)
    max_value = np.max(arr)
    
    if min_value == max_value:
        return np.zeros_like(arr)
    return (arr - min_value)/(max_value - min_value)

def standardize_array(arr):
    """
    Standardizes a NumPy array using Z-score normalization.
    The transformed data will have a mean of 0 and a standard deviation of 1.
    """
    mean_val = np.mean(arr)
    std_dev = np.std(arr)
    if std_dev == 0:
        return np.zeros_like(arr)  # Avoid division by zero
    return (arr - mean_val) / std_dev

# Usage of normalize function
data = np.array([5, 15, 25, 35, 45])
normalized_data = normalize_array(data)
standardized_data = standardize_array(data)

print("Original Array:", data)
print("Normalized Array:", normalized_data)
print("Standardized Array:", standardized_data)