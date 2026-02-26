# numpy filter 
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = []

for x in arr:
    if x > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

print(filter_arr)           