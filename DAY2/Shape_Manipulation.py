# SHAPE MANIPULATION

'''

 Change Shape

    • reshape()
    • resize()

Convert into 1D

    • flatten()
    • ravel()

Change Direction

    • transpose()
    • swapaxes()

Remove Dimension

    • squeeze()

 Add Dimension

    • expand_dims()

Minimum Dimension

    • atleast_1d()
    • atleast_2d()
    • atleast_3d()

'''

# Change Shape

    # reshape()

            # reshape() is used to change the shape of an array.
            # It does not change the original array.
            # It only changes how the data is arranged.

        # Total Number of Elements Must Remain Same

    # Main Purpose

        # reshape() is used to:

            # Change the shape of an array.
            # Convert 1D array to 2D or 3D.
            # Convert 2D array to another shape.
            # Prepare data for Machine Learning and Deep Learning models


import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr)

arr1=arr.reshape(2,3)
print(arr1)

# Output
'''
[[10 20 30]
 [40 50 60]] 
'''

# Data is same 
# only chnage shape


# Example: 

import numpy as np

arr = np.arange(6)

print("Original Array")
print(arr)

new_arr = arr.reshape(2,3)

print("\nReshaped Array")
print(new_arr)

print("-----------------------------------")

# Example:

arr=np.arange(10)
print(arr)
print()
print(arr.reshape(5,2))

print("-----------------------------------")

arr=np.arange(9)
print(arr)
print()

print(arr.reshape(3,3))

print("-----------------------------------")

arr=np.arange(12)
print("Orginal Shape",arr.shape)

new=arr.reshape(2,6)

print("New Shape:",new.shape)
print(new)

print("-----------------------------------")

arr = np.arange(12)
print(arr.reshape(-1,2))

print("-----------------------------------")

arr = np.arange(20)
print(arr.reshape(5,-1))

print("-----------------------------------")

arr=np.arange(24)

new=arr.reshape(2,4,3)
print(new)

print("-----------------------------------")


arr=np.arange(6)

new=arr.reshape(2,3)

new[0][0]=100

print("Original Array")
print(arr)

print()

print("Reshape Array")
print(new)

# Suppose an image has 16 pixels.

image = np.arange(16)

image = image.reshape(4,4)

print(image)
print()

    # resize()

        # resize() is used to change the shape of the original array.

arr=np.arange(12)
arr.resize(3,4)
print(arr)

# Resize to larger

arr=np.arange(5)
arr.resize(10)
print(arr)

# Output [0 1 2 3 4 0 0 0 0 0]
# Extra positions are filled with 0.

# Resize to a Smaller Size

arr=np.arange(10)
arr.resize(5)
print(arr)

# [0 1 2 3 4]
# Extra elements are removed.

'''

reshape() vs resize()

| reshape()                        | resize()                                    |
| -------------------------------- | ------------------------------------------- |
| Returns a new array              | Changes the original array                  |
| Number of elements cannot change | Number of elements can increase or decrease |
| Safe to use                      | Changes original data                       |
| Used more often                  | Used less often                             |

'''

# flatten()

        # flatten() converts any array into a 1D array.

arr=np.array([
    [1,2,3],
    [4,5,6]
])

arr1=arr.flatten()
print(arr1)

# Copy Example

    # The original array did not change.

arr1[0]=100

print(arr)
print(arr1)

# ravel()

    # ravel() also converts an array into a 1D array.
    # But it usually returns a view to avoid of a copy.
    # The original array also changed.

arr=np.array([
    [1,2,3],
    [4,5,6]
])

new=np.ravel(arr)
print(new)

new[0]=100

print(new)
print(arr)

# flatten() vs ravel()

'''
| flatten()                  | ravel()                  |
| -------------------------- | ------------------------ |
| Returns a copy             | Returns a view (usually) |
| Original remains unchanged | Original may change      |
| Slower                     | Faster                   |
| Safer                      | Uses less memory         |

'''

# transpose()

    # transpose() swaps rows and columns.
    # Rows become Column
    # Column become Rows

arr=np.array([
    [1,2,3],
    [4,5,6]
])

print(arr.T)

arr=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

new=arr.T
print(new)

# swapaxes()

    # swapaxes() exchanges any two axes.
    # It is mainly useful for 3D or higher-dimensional arrays.

# Give me correct example

arr=np.array([[
    [1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3],
]])

print(arr.shape)
arr.swapaxes(0,1)
print(arr.shape)

# transpose() vs swapaxes()

'''
| transpose()                | swapaxes()                   |
| -------------------------- | ---------------------------- |
| Changes all axes           | Swaps only two selected axes |
| Mostly used with 2D arrays | Mostly used with 3D arrays   |

'''

# squeeze()

        # squeeze() removes dimensions whose size is 1.

arr1=np.array([[[1],[2],[3],[4],[5]]])

print(arr1.shape)

# Output (1,5,1)

arr=np.squeeze(arr1)
print(arr.shape)

# Output (5,)

# expand_dims()

        # expand_dims() adds a new dimension to an array.

# orginal shape (5,)

arr=np.array([1,2,3,4,5])
new=np.expand_dims(arr,axis=0)
print(new.shape)


# atleast_1d()

        # Ensures that the input has at least one dimension.

a=5

print(np.atleast_1d(a))

# atleast_2d()

        # Ensures that the input has at least two dimensions.

a=5

print(np.atleast_2d(a))

# atleast_3d()

        # Ensures that the input has at least three dimensions.

a=5

print(np.atleast_3d(a))


print("--------------------------------------------------------------------")

print("---------------------- Shape Manipulation Practice ----------------------------")

# Q1 Create a 1D array containing numbers from 1 to 12 and reshape it into (3,4).

import numpy as np

arr=np.arange(1,13)
print(arr)

new=arr.reshape(3,4)
print(new)
print()
# Q2 Create an array of 20 elements and reshape it into (4,5).

arr=np.arange(1,21)
print(arr)

print(arr.reshape(4,5))
print()

# Q3 Create an array of 16 elements and reshape it into a 4×4 matrix.

arr=np.arange(1,17)
print(arr)

print(arr.reshape(4,4))
print()

# Q4 Create an array of 24 elements and reshape it into (2,3,4).

arr=np.arange(24)
print(arr)

print(arr.reshape(2,3,4))
print()

# Q5 Create an array of 18 elements and reshape it using -1 so NumPy automatically calculates the number of rows.

arr=np.arange(18)
new=arr.reshape(-1,3)
print(new)
print()

# Q6 Create a (3,4) array.

arr=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
])

print(arr)

    # Convert it into 1D using:

# flatten()
new=arr.flatten()

# ravel()
new1=arr.ravel()


# Print both arrays.

print(new)
print(new1)

print()

# Q7 Modify the first element of the flattened array.

    # Check whether the original array changes.

new[0]=100

print(arr)
print(new)

print()

# Original element is not change

# Q8 Modify the first element of the ravel array.

    # Check whether the original array changes.
    # Explain why.

new1[0]=101
print(arr)
print(new1)

print()

# Original aaray is change
# because faltten cretae a copy of origial array 
# ravel create a view of original array

# Q9 Create a (2,3) array.

arr=np.array([
    [11,12,13],
    [14,15,16]
])

print(arr)
    # Transpose it.

new=arr.transpose()
print(new)

# Print:
# Original Shape
print(arr.shape)

# New Shape
print(new.shape)

# Q10 Create a 3D array of shape (2,3,4).

arr=np.array([
    [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    ],
    [
        [13,14,15,16],
        [17,18,19,20],
        [21,22,23,24],
    ]
    ])

print(arr)

# Use swapaxes() to exchange:
    # axis 0 and axis 1

new1=arr.swapaxes(0,1)
print(new1.shape)

    # axis 1 and axis 2

new2=arr.swapaxes(1,2)
print(new2.shape)

# Print the shape after each operation.

# Q11 Create the following array.

# [[[1]
# [2]
#  [3]]]

arr=np.array([
    [
    [1],
    [2],
    [3]
    ]
])
print(arr)

# Print:
# Shape before squeeze()
print(arr.shape)

# Shape after squeeze()

new=arr.squeeze()
print(new)
print(new.shape)

# Q12 Create a 1D array.

arr=np.array([1,2,3,4,5])

# Use expand_dims() to add:

# axis=0

new=np.expand_dims(arr,axis=0)
print(new)

# axis=1

new1=np.expand_dims(arr,axis=1)
print(new1)

# Print both shapes.
print(new.shape)
print(new1.shape)

# Q13 Convert the integer
# 5
a=5


# into:

    # atleast_1d
    # atleast_2d
    # atleast_3d

one= np.atleast_1d(a)
two= np.atleast_2d(a)
three= np.atleast_3d(a)

# Print the shapes.
print(one.shape)
print(two.shape)
print(three.shape)

# Q14 Create a (2,6) array.

arr=np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
])
print(arr)

# Reshape it into:

# (3,4)
re1=arr.reshape(3,4)
print(re1)

# (4,3)
re2=arr.reshape(4,3)
print(re2)
    
# (2,2,3)
re3=arr.reshape(2,2,3)
print(re3)

# Print every shape.
print(re1.shape)
print(re2.shape)
print(re3.shape)

# Q15 
# Create an array of 48 elements.

arr=np.arange(48)
print(arr)

# Perform all of the following:

    # reshape()
res=arr.reshape(8,6)
print(res)

# flatten()

cop=arr.flatten()
cop[0]=100

print(arr)
print(cop)
print()

# ravel()

cop1=arr.ravel()
cop1[0]=101
print(arr)
print(cop1)

# transpose()

tran=np.transpose(res)
print(tran)

# expand_dims()

ex=np.expand_dims(arr,axis=0)
print(ex)

# squeeze()

ex1=np.squeeze(arr)
print(ex1)

# Print the shape after every step.

print(arr.shape)

print(res.shape)

print(cop.shape)

print(cop1.shape)

print(tran.shape)

print(ex.shape)

print(ex1.shape)