# list containing numbers
List = [1, 2, 3, 4, 5, 6]

# printing the address of the List itself
print(f"Address of the List object : {id(List)}")

# printing the address of each Python int object
for i in List:
    print(f"{i} : {id(i)}")

import numpy as np

# create a 1D numpy array
Array = np.array(List, dtype=np.int32)

print(f"\nAddress of the NumPy Array object : {id(Array)}")

# printing the C memory addresses of each element
print("Element values with their memory addresses:")
for i in range(Array.size):
    addr = Array.ctypes.data + i * Array.itemsize
    print(f"{Array[i]} : {addr}")
