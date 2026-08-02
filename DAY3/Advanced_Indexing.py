# Advanced Indexing

        # 1. Fancy Indexing
        # 2. Boolean Indexing

# ==========================================================
# FANCY INDEXING
# ==========================================================

        # Fancy Indexing means
        # selecting multiple elements
        # using a list or array of indexes.

        # In normal indexing,
        # we can select only one index at a time.

# Example

# arr[2]

# Here,
# only one element is selected.

# But suppose we want

# index 0
# index 3
# index 5

# at the same time.

# Normal indexing cannot do this.

# Fancy Indexing solves this problem.


# Example 

# array[[0,4,7]]

# Notice

# Double square brackets

# Outer [] = indexing operator

# Inner [] = list of indexes

import numpy as np

arr=np.array([10,20,30,40,50,60,70,80,90,100])
print(arr[[0,4,7]])

# Duplicate Indexes

print(arr[[1,1,1,2]])

# Fancy Indexing in 2D Array

arr=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(arr[[0,2]])
print(arr[[2,0]])

print(arr[[0,2],[1,2]])

# Row indexes    -> [0,2]
# Column indexes -> [1,2]

# Pairing

# (0,1) -> 20
# (2,2) -> 90

# Output
# [20 90]

# -------------------------------------------------------------------------------

# BOOLEAN INDEXING

        # Boolean Indexing means
        # selecting elements using
        # True and False values.

        # Instead of selecting elements
        # using indexes,
        # we select them using CONDITIONS.

# Condition Examples

# >
# <
# >=
# <=
# ==
# !=

# Every condition returns

        # True
        # or
        # False

        # NumPy then selects
        # only those elements
        # whose value is True.


# Syntax

# array[condition]

# Example

# arr[arr > 20]

# Read it as

# Select all elements
# where value is greater than 20.

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr>7)

print(arr[arr>7])
print(arr[arr<=4])
print(arr[arr%2==0])
print(arr[arr%2!=0])

arr1=np.array([50,100,150,50,200,100,50,100,100])
result=arr1[arr1==100]
print(len(result))

# Boolean Indexing in 2D Array

arr=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(arr[arr>50])

# Multiple Conditions

arr=np.array([10,20,30,40,50,60])

print(arr[(arr>20) & (arr<60)])

# OR Condition

arr=np.array([10,20,30,40,50])

print(arr[(arr<20) | (arr>40)])

# NOT Condition

arr=np.array([10,20,30,40])

print(arr[~(arr>20)])

# Boolean Assignment

arr=np.array([10,20,30,40,50])

arr[arr>30]=0

print(arr)
