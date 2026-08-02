# Q1 Create the following array.

# [10,20,30,40,50,60]

# Print
# [20 30 40]

import numpy as np
arr=np.array([10,20,30,40,50,60,])

print(arr[1:4])

# Q2 Create the following array.
# [100,200,300,400,500,600]

# Print
# [100 200 300]

arr=np.array([100,200,300,400,500,600])

print(arr[0:3])

# Q3 Create the following array.
# [5,10,15,20,25,30]

# Print
# [20 25 30]

arr=np.array([5,10,15,20,25,30])

print(arr[3:])

# Q4 Create the following array.
# [11,22,33,44,55,66]

# Print
# [22 33]

arr=np.array([11,22,33,44,55,66])

print(arr[1:3])
    
# Q5 Create the following array.
# [1,2,3,4,5,6,7,8]

# Print
# [3 4 5 6]

arr=np.array([1,2,3,4,5,6,7,8])
print(arr[2:6])

# Q6 Create the following array.
"""
[
 [10,20,30],
 [40,50,60],
 [70,80,90]
]
"""

# Print

"""
[
 [10 20]
 [40 50]
]
"""

arr=np.array([

 [10,20,30],
 [40,50,60],
 [70,80,90]

])

print(arr[0:2,0:2])

# Q7

# Using the same array

# Print

"""
[
 [20 30]
 [50 60]
]
"""

arr=np.array([

 [10,20,30],
 [40,50,60],
 [70,80,90]

])
print(arr[0:2,1:])

# Q8

# Using the same array

# Print

"""
[
 [40 50 60]
 [70 80 90]
]
"""

arr=np.array([

 [10,20,30],
 [40,50,60],
 [70,80,90]

])
print(arr[1:,:])

# Q9

# Using the same array

# Print

"""
[
 [20]
 [50]
 [80]
]
"""

arr=np.array([

 [10,20,30],
 [40,50,60],
 [70,80,90]

])
print(arr[:,1:2])



# Q10

# Using the same array

# Print

"""
[
 [50 60]
 [80 90]
]

"""


arr=np.array([

 [10,20,30],
 [40,50,60],
 [70,80,90]

])
print(arr[1:,1:])

# Q11 Create the following 3D array.

"""
[
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

"""
[
 [1 2]
 [3 4]
]
"""

arr=np.array(
    [
    [
        [1,2],
        [3,4]
    ],

    [
        [5,6],
        [7,8]
    ]
]
)

print(arr[0,:,:])

# Q12

# Using the same array

# Print

"""
[
 [5 6]
 [7 8]
]
"""
arr=np.array(
    [
    [
        [1,2],
        [3,4]
    ],

    [
        [5,6],
        [7,8]
    ]
]
)

print(arr[1,:,:])

# Q13

# Using the same array

# Print

"""
[
 [3 4]
]
"""

arr=np.array(
    [
    [
        [1,2],
        [3,4]
    ],

    [
        [5,6],
        [7,8]
    ]
]
)

print(arr[0,1:2,:])

# Q14

# Using the same array

# Print

"""
[
 [2]
 [4]
]
"""

arr=np.array(
    [
    [
        [1,2],
        [3,4]
    ],

    [
        [5,6],
        [7,8]
    ]
]
)

print(arr[0,:,1:])

# Q15 ⭐ Challenge

# Create the following 3D array.

"""
[
    [
        [10,20,30],
        [40,50,60]
    ],

    [
        [70,80,90],
        [100,110,120]
    ]
]
"""

# Without using loops, print

# Output 1
"""
[
 [20 30]
 [50 60]
]
"""

arr=np.array([
    [
        [10,20,30],
        [40,50,60]
    ],

    [
        [70,80,90],
        [100,110,120]
    ]
]
)

print(arr[0,:,1:])

# Output 2
"""
[
 [70 80 90]
 [100 110 120]
]
"""

[
    [
        [10,20,30],
        [40,50,60]
    ],

    [
        [70,80,90],
        [100,110,120]
    ]
]

print(arr[1,:,:])

# Output 3
"""
[
 [50]
 [110]
]
"""

[
    [
        [10,20,30],
        [40,50,60]
    ],

    [
        [70,80,90],
        [100,110,120]
    ]
]

print(arr[:,1:,1])