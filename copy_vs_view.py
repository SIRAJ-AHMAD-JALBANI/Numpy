import numpy as np
#copy is a new array object and view is a view of the original array

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x)
print(y)

# Make a view, change the original array, and display both arrays:

arr[0] = 42
print(arr)
print(x)
print(y)    

# Make Changes in the VIEW:

y[0] = 42
print(arr)
print(x)
print(y)

# Make Changes in the COPY:

x[0] = 42
print(arr)
print(x)
print(y)
