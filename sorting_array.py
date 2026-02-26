# sorting array
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

# Sort the array alphabetically:

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

# Sort a 2-D array:

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

# Sort the array by the second column:

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr, axis=1)) # Sort the array by the second column:              
