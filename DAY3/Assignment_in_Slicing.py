# ASSIGNMENT IN SLICING

        # Assignment in slicing means
        # replacing the values of a slice
        # with new values.

        # Instead of only selecting data,
        # we MODIFY the selected part.

        # Syntax
        # array[start:stop] = values

        # Rules

        # 1. Left side = Slice to modify
        # 2. Right side = New values
        # 3. Number of values should match
        #    the selected elements
        #    (unless using a single value).


# Example

import numpy as np

arr = np.array([10,20,30,40,50])

arr[1:4] = [100,200,300]

print(arr)

# Output

# [ 10 100 200 300  50 ]

# -------------------------------------------------------------------

# Replace with Single Value

import numpy as np

arr = np.array([10,20,30,40,50])

arr[1:4] = 0

print(arr)

# Output

# [10  0  0  0 50]

# -------------------------------------------------------------------

# Replace Entire Array

import numpy as np

arr = np.array([10,20,30,40])

arr[:] = [1,2,3,4]

print(arr)

# Output

# [1 2 3 4]

# -------------------------------------------------------------------

# Replace Every Second Element

import numpy as np

arr = np.array([10,20,30,40,50,60])

arr[::2] = [100,200,300]

print(arr)

# Output

# [100  20 200  40 300  60]

# -------------------------------------------------------------------

# Reverse Assignment

import numpy as np

arr = np.array([10,20,30,40,50])

arr[::-1] = arr

print(arr)

# Output

# [50 40 30 20 10]

# -------------------------------------------------------------------

# 2D Assignment

import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

arr[0] = [1,2,3]

print(arr)

# Output

# [[ 1  2  3]
#  [40 50 60]
#  [70 80 90]]

# -------------------------------------------------------------------

# Replace a Column

import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

arr[:,1] = [100,200,300]

print(arr)

# Output

# [[ 10 100  30]
#  [ 40 200  60]
#  [ 70 300  90]]

# -------------------------------------------------------------------

# Replace Multiple Rows

import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

arr[0:2] = [
    [1,2,3],
    [4,5,6]
]

print(arr)

# Output

# [[ 1  2  3]
#  [ 4  5  6]
#  [70 80 90]]

# -------------------------------------------------------------------

# Replace Multiple Columns

import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

arr[:,0:2] = [
    [1,2],
    [3,4],
    [5,6]
]

print(arr)

# Output

# [[ 1  2 30]
#  [ 3  4 60]
#  [ 5  6 90]]