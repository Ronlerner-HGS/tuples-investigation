import numpy as np

fruits = ['apple', 'banana', 'cherry', 'date']

lengths = np.array([len(fruit) for fruit in fruits])

doubled_lengths = lengths * 2

print("Original lengths:", lengths)
print("Doubled lengths:", doubled_lengths)