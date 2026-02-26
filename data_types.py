import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr2 = np.array(['apple', 'banana', 'cherry'])

print(arr2.dtype)

arr3 = np.array([1, 2, 3, 4], dtype='S')

print(arr3.dtype)

#  creating array with a defined data type
arr4 = np.array([1, 2, 3, 4], dtype='i4')

print(arr4.dtype)

#  creating array with a defined data type
arr5 = np.array([1, 2, 3, 4], dtype='f4')

print(arr5.dtype)

#  creating array with a defined data type
arr6 = np.array([1, 2, 3, 4], dtype='f4')   

# size of the array
# Create an array with data type 4 bytes integer:

arr7 = np.array([1, 2, 3, 4], dtype='i4')

print(arr7.nbytes)

# size of the array
# Create an array with data type 4 bytes integer:

