# 3D Slicing

        # 3D Slicing is an extension of 2D Slicing.

        # 3D Slicing means selecting Blocks, Rows, and Columns
        # from a 3D array.

        # A 3D array has three dimensions:
        
        # 1. Block (Depth)
        # 2. Row
        # 3. Column

        # array[block, row, column]

import numpy as np

arr=np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])
print(arr.shape)

# Access Element

# First block
print(arr[0])

# Second block
print(arr[1])

# First row of first block
print(arr[0,0])

# Second row of second block
print(arr[1,1])

# Single Element
print(arr[1,1,2])

# Slicing

# Take only first block
print(arr[0:1,:,:])

# Take both blocks
print(arr[:,:,:])

# Take first row from every block
print(arr[:,0,:])

# Take second row from every block
print(arr[:,1,:])

# Take first column from every block
print(arr[:,:,0])

# Take last column
print(arr[:,:,2])

# Take first two columns
print(arr[:,:,0:2])

# Take only Block 1 and Row 0
print(arr[1,0])

# Take Block 0 and first two columns
print(arr[0,:,0:2])

# Last Column of First Block
print(arr[1,:,2])