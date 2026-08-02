# Splitting Arrays

        # Divide one array into multiple arrays.

        # We use splitting when we want to:

            # Divide large datasets
            # Split training and testing data
            # Process data in smaller parts
            # Analyze different sections of data
            # Perform batch processing
        
# Types of Splitting Arrays

    # split()
    # hsplit()
    # vsplit()
    # dsplit()
    # array_split()

# split()

        # split() divides an array into equal-sized parts.
        # If equal division is not possible, it gives an error.

import numpy as np

arr=np.arange(8)
print(np.split(arr,4))

print()

arr=np.array([2,4,6,8,10,12,14,16])
print(np.split(arr,2))

# hsplit()

        # hsplit() means Horizontal Split.
        # It splits an array column-wise (Left → Right).
        # main purpose of hsplit is Divide columns

print()

arr=np.array([2,4,6,8,10,12,14,16])

print(arr)
print(np.hsplit(arr,4))

# vsplit()

        # vsplit() means Vertical Split.
        # It splits an array row-wise (Top → Bottom).
        # main purpose of vsplit is Divide rows

arr=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [16,17,18,19,11],
    [26,27,28,29,21]
])
print()
print(np.vsplit(arr,4))

# dsplit()

        # dsplit() means Depth Split.

        # It splits an array along the third dimension (depth).

        # Mostly used for 3D arrays.

        # main purpose of dsplit is Divide depth layers

arr=np.array([[[
    [2,4,6,8,10,12,14,16],
    [2,4,6,8,10,12,14,16],
    ]]])
print()
print(np.dsplit(arr,2))


# array_split()

        # array_split() is similar to split().
        # but the difference is

                # split() requires equal division.
                # array_split() allows unequal division.

arr=np.arange(10)
print(np.array_split(arr,3))

# Output is  [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]


# split() vs array_split()

'''
| split()                       | array_split()                       |
| ----------------------------- | ----------------------------------- |
| Equal division only           | Equal or unequal division           |
| Gives error if not possible   | Never gives error for uneven splits |
| Used when data divides evenly | More flexible                       |

'''

# hsplit() vs vsplit()

'''

| hsplit()         | vsplit()       |
| ---------------- | -------------- |
| Splits columns   | Splits rows    |
| Left → Right     | Top → Bottom   |
| Horizontal split | Vertical split |

'''

print("---------------------------------------")
# Q1 Create an array of 12 elements.

# Split it into 3 equal parts using split().

arr=np.arange(12)
print(np.split(arr,3))
print()

# Q2 Create an array of 16 elements.

# Split it into 4 equal parts.

arr=np.arange(16)
print(np.split(arr,4))
print()

# Q3 Create a (4,4) array.

# Use vsplit() to split it into 2 parts.

arr=np.array([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],

])
res=np.vsplit(arr,2)
print(res)
print()

# Q4 Create a (4,4) array.

# Use hsplit() to split it into 2 parts.

arr=np.array([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],

])
res=np.hsplit(arr,2)
print(res)
print()

# Q5 Create an array of 10 elements.

# Split it using array_split() into 3 parts.

arr=np.arange(10)
res=np.array_split(arr,3)
print(res)
print()

# Q6 Create a (6,6) array.

arr=np.array([
        [1,2,3,4,5,6],
        [5,6,7,8,9,10],
        [11,12,13,14,15,16],
        [16,17,18,19,20,21],
        [22,23,24,25,26,27],
        [28,29,30,31,32,33],
])

# Split it into:

# 3 vertical parts

res=np.vsplit(arr,3)
print(res)
print()

# 2 horizontal parts

res=np.hsplit(arr,2)
print(res)
print()

# Q7 Create a (2,2,4) array.

arr=np.array([
        [
                [1,2,3,4],
                [5,6,7,8]
        ],

        [
                [9,10,11,12],
                [13,14,15,16]
        ],   
])

print(arr)

# Use dsplit() to split it into 2 depth parts.

res=np.dsplit(arr,2)
print(res)

# Q8 Create an array of 15 elements.

arr=np.arange(15)
print(arr)

# Split it into 5 equal parts.

res=np.split(arr,5)
print(res)

# Q9 Create an array of 14 elements.

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
print(arr)
print()

# Try using split().

res=np.split(arr,2)
print(arr)

# Observe the error.

# it not return error but it return whole array

# Then solve it using array_split().

res=np.array_split(arr,2)
print(arr)

# Q10 Create a (8,4) array.

arr=np.array([
        [1,2,3,4],
        [11,12,13,14],
        [21,22,23,24],
        [31,32,33,34],
        [41,42,43,44],
        [51,52,53,54],
        [61,26,63,64],
        [71,72,73,74],
]
)

# Split it vertically into 4 parts.

res=np.vsplit(arr,4)
print(res)


# Print the shape of every part.

for part in res:
    print(part.shape)


# Q11 Create a (6,6) array.

arr=np.array([
        [1,2,3,4,5,6],
        [11,12,13,14,15,16],
        [21,22,23,24,25,26],
        [31,32,33,34,35,36],
        [41,42,43,44,45,46],
        [51,55,53,54,55,56],
])

# Split columns into 3 parts using hsplit().

res=np.hsplit(arr,3)
print(res)
print()

# Q12 Create a (9,3) array.

arr=np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12],
        [13,14,15],
        [16,17,18],
        [19,20,21],
        [22,23,24],
        [25,26,27]
])

# Split rows into 3 equal parts using vsplit().

res=np.vsplit(arr,3)
print(res)

# Q13 Create a (2,4,6) array.

arr=np.arange(48)
print(arr)

res=arr.reshape(2,4,6)
print(res)

# Use dsplit() to split it into 3 equal depth parts.

# res=np.dsplit(arr,3)
print(res)

# Print the shape of every output.
print(np.shape(res))
print()
# Q14 Create an array of 25 elements.

arr=np.arange(25)
print(arr)

# Split it into 6 parts using array_split().

print(np.array_split(arr,6))
print()

# Print the length of each part.

for i in np.array_split(arr,6):
    print(len(i))

# Q15 Create a (6,6) array.

arr= np.array([
        [1,2,3,4,5,6],
        [11,12,13,14,15,16],
        [21,22,23,24,25,26],
        [31,32,33,34,35,36],
        [41,42,43,44,45,46],
        [51,52,53,54,55,56],
])

# Perform all of the following:

# split()

print(np.split(arr,6))
print()

# hsplit()

print(np.hsplit(arr,6))
print()

# vsplit()

print(np.vsplit(arr,6))
print()

# dsplit() (after reshaping appropriately)


arr=np.arange(72).reshape(2,6,6)

res=np.dsplit(arr,3)

#     raise ValueError('dsplit only works on arrays of 3 or more dimensions')

# array_split()

print(np.array_split(arr,6))
print()

# For each operation, print:

# Original shape
print(arr.shape)

# Number of resulting arrays
print(len(res))

# Shape of each resulting array

for part in res:
    print(part.shape)