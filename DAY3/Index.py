# Index

        # An index is the position of an element inside an array.
        # 10 20 30 40 50 
            # 10 index is 0
            # 20 index is 1
            # 30 index is 2
            # 40 index is 3
            # 50 index is 4
        # Index Start from zero
        # reverse Index Start from -1

import numpy as np

arr=np.array([10,20,30,40,50])

print(arr[0])
print(arr[1])
print(arr[-1])
print(arr[-2])

# update element using index

arr[0]=100

print(arr)

# Type of Index 
    # Positive Index
    # Negative Index

    # positive Index

        # Positive indexing always starts from 0.
        # It access the element from the array left side to right

        # Index : 0 1 2 3 4 
        # Value : 10 20 30 40 50

    # Negetive Index

        # Negative indexing always starts from -1.
        # It access the element from the array end or right side to left side of array

        # Negative Index : -5 -4 -3 -2 -1 
        # Value : 10 20 30 40 50


# Multi-dimensional Indexing (2D Array)

# What is a 2D Array?

    # A 2D array contains Rows and Columns.

    # It looks similar to an Excel worksheet or a table.

# Example:  

arr=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [12,14,15,16],
])

print(arr)
print(arr[1,1])
print(arr[2,2])
print(arr[-1,-1])
print(arr[-2,-1])
print(arr[-1,-2])

# update

arr[3,0]=999
print(arr)


# Multi-dimensional Indexing (3D Array)

        # A 3D array is an array that contains multiple 2D arrays.
        # A 3D array has three dimensions:

            # Depth (Layer)
            # Row
            # Column

        # if we access the element from 3D array then we need three indexs

        # A 3D array has Layers, Rows, and Columns.
        
        # array[layer,row,column]

arr= np.array([
    [
        [1,2,3,4],
        [11,12,13,14]

    ],

    [
        [21,22,23,24],
        [31,32,33,34]
    ]
])

print(arr)

print(arr[0,0,0])
print(arr[0,1,3])

print(arr[1,1,2])
print(arr[1,0,1])

print(arr[-1,-1,-1])
print(arr[-1,-2,-3])

# Update 

arr[0,0,0]=111
print(arr)

arr[1,1,3]=222
print(arr)

# -----------------------------------------------------------------------------
#    Practice
# -----------------------------------------------------------------------------


# Q1 Create the following array.

# [10,20,30,40,50]

# Print the first element.

# Expected Output
# 10

import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[0])

# Q2 Create the following array.

# [100,200,300,400,500]

# Print the last element using positive indexing only.

# Expected Output

# 500

arr=np.array([100,200,300,400,500])
print(arr[4])

# Q3 Create the following array.

# ["Python","Java","C++","SQL"]

# Print

# Java

arr=np.array(["Python","Java","C++","SQL"])
print(arr[1])

# Q4 Create the following array.

# [5,10,15,20,25]

# Print

# 15

arr=np.array([5,10,15,20,25])
print(arr[2])

# Q5 Create the following array.

# [11,22,33,44,55]

# Print the second last element using negative indexing.

# Expected Output

# 44

arr=np.array([11,22,33,44,55])
print(arr[-2])

# Q6 Create the following array.

"""[
 [10,20,30],
 [40,50,60],
 [70,80,90]
]"""

# Print

# 50

arr=np.array([
  [10,20,30],
 [40,50,60],
 [70,80,90]
])

print(arr[1,1])

# Q7

# Using the same array

# Print

# 90

# using negative indexing only.

arr=np.array([
  [10,20,30],
 [40,50,60],
 [70,80,90]
])

print(arr[-1,-1])


# Q8 Using the same array

# Print

# 20

arr=np.array([
  [10,20,30],
 [40,50,60],
 [70,80,90]
])

print(arr[0,1])

# Q9 Using the same array

# Print

# 70

arr=np.array([
  [10,20,30],
 [40,50,60],
 [70,80,90]
])

print(arr[2,0])

# Q10

# Using the same array

# Print these values one by one.

# 30

# 50

# 70

# (No slicing allowed.)

arr=np.array([
  [10,20,30],
 [40,50,60],
 [70,80,90]
])

print(arr[0,2])
print(arr[1,1])
print(arr[2,0])

# Q11 Create the following 3D array.

"""[
    [
        [1,2],
        [3,4]
    ],

    [
        [5,6],
        [7,8]
    ]
]
"""
# Print

# 1

arr=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]

])

print(arr[0,0,0])

# Q12 Using the same array

# Print

# 8

# using negative indexing only.

arr=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]

])

print(arr[1,-1,-1])


# Q13 Using the same array

# Print

# 6
arr=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]

])

print(arr[1,0,1])

# Q14 Using the same array

# Print

# 3

# 5

# 8

# (one by one)

arr=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]

])

print(arr[0,1,0])
print(arr[1,0,0])
print(arr[1,1,1])


# Q15 ⭐ Challenge  Create this 3D array.
arr=np.array(
[
    [
        [10,20,30],
        [40,50,60]
    ],

    [
        [70,80,90],
        [100,110,120]
    ]
])

# Without using slicing, print:

# 10

# 50

# 90

# 120

print(arr[0,0,0])
print(arr[0,1,1])
print(arr[1,0,2])
print(arr[1,1,2])
