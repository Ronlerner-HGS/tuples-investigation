import numpy as np

numbers_list = list(range(1, 11))

numbers_array = np.array(numbers_list) * 5

print("Original list:", numbers_list)
print("Numpy array after multiplication:", numbers_array)