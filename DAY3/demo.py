# Q1 Create the following array.

# [10,20,30,40,50]

# Using a basic for loop,
# print every element.

# Expected Output

# 10
# 20
# 30
# 40
# 50

import numpy as np
arr=np.array([10,20,30,40,50])

for i in arr:
    print(i)

# ----------------------------------------------------------

# Q2 Create the following array.

# ["Python","Java","SQL","C++"]

# Using a basic for loop,
# print every language.

arr=np.array(["Python","Java","SQL","C++"])

for i in arr:
    print(i)

# ----------------------------------------------------------


# Q3 Create the following 2D array.

"""
[
 [10,20],
 [30,40]
]
"""

# Using one for loop,
# print each row.

# Expected Output

# [10 20]
# [30 40]

arr=np.array([
 [10,20],
 [30,40]
])

for i in arr:
    print(i)

# ----------------------------------------------------------

# Q4

# Using the same array,

# Print every element
# using nested for loops.

# Expected Output

# 10
# 20
# 30
# 40

arr=np.array([
 [10,20],
 [30,40]
])

for i in arr:
    for v in i:
        print(v)

# ----------------------------------------------------------


# Q5 Create the following 3D array.

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

# Using basic iteration,

# Print each 2D block.

# Expected Output

"""
[[1 2]
 [3 4]]

[[5 6]
 [7 8]]
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
])

for i in arr:
    print(i)

# Q6

# Using the following array.

"""
[
 [10,20],
 [30,40]
]
"""

# Use np.nditer()

# Print every element.

# Expected Output

# 10
# 20
# 30
# 40

arr=np.array(
    [
 [10,20],
 [30,40]
]
)

for i in np.nditer(arr):
    print(i)

# ----------------------------------------------------------

# Q7 Create the following array.

"""
[
 [100,200,300],
 [400,500,600]
]
"""

# Use np.nditer()

# Print every value.

arr=np.array(
    [
 [100,200,300],
 [400,500,600]
]
)

for i in np.nditer(arr):
    print(i)

# ----------------------------------------------------------

# Q8 Create the following 3D array.

"""
[
    [
        [10,20],
        [30,40]
    ],

    [
        [50,60],
        [70,80]
    ]
]
"""

# Use np.nditer()

# Print every element.

# Expected Output

# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80

arr=np.array([
    [
        [10,20],
        [30,40]
    ],

    [
        [50,60],
        [70,80]
    ]
])

for i in np.nditer(arr):    
    print(i)
# ----------------------------------------------------------


# Q9 Create the following array.

"""
[
 [5,10,15],
 [20,25,30]
]
"""

# Use np.nditer()

# Print every value multiplied by 2.

# Expected Output

# 10
# 20
# 30
# 40
# 50
# 60

arr=np.array([
 [5,10,15],
 [20,25,30]
])

for i in np.nditer(arr):
    print(i*2)
# ----------------------------------------------------------


# Q10 Create the following array.

# [1,2,3,4,5]

# Use np.nditer()

# Print the square
# of every element.

# Expected Output

# 1
# 4
# 9
# 16
# 25

arr=np.array([1,2,3,4,5])

for i in np.nditer(arr):
    print(i*i)

# ==========================================================

# Q11 Create the following array.

# [10,20,30]

# Use np.ndenumerate()

# Print both
# index and value.

# Expected Output

# (0,) 10
# (1,) 20
# (2,) 30

arr=np.array([10,20,30])

for idx,val in np.ndenumerate(arr):
    print(idx,val)

# ----------------------------------------------------------


# Q12 Create the following array.

"""
[
 [10,20],
 [30,40]
]
"""

# Use np.ndenumerate()

# Expected Output

# (0,0) 10
# (0,1) 20
# (1,0) 30
# (1,1) 40

arr=np.array(
    [
 [10,20],
 [30,40]
]
)

for idx,val in np.ndenumerate(arr):
    print(idx,val)

# ----------------------------------------------------------

# Q13 Create the following 3D array.

"""
[
    [
        [1,2],
        [3,4]
    ]
]
"""

# Use np.ndenumerate()

# Expected Output

# (0,0,0) 1
# (0,0,1) 2
# (0,1,0) 3
# (0,1,1) 4

arr=np.array(
    [
    [
        [1,2],
        [3,4]
    ]
]
)

for idx,val in np.ndenumerate(arr):
    print(idx,val)
# ----------------------------------------------------------


# Q14 Create the following array.

"""
[
 [100,200,300],
 [400,500,600]
]
"""

# Using np.ndenumerate()

# Print like this.

# Index: (0,0) Value: 100
# Index: (0,1) Value: 200
# Index: (0,2) Value: 300
# Index: (1,0) Value: 400
# Index: (1,1) Value: 500
# Index: (1,2) Value: 600


arr=np.array(
    [
 [100,200,300],
 [400,500,600]
]
)

for idx,val in np.ndenumerate(arr):
    print(idx,val)
# ----------------------------------------------------------


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

# Using np.ndenumerate()

# Print

# Index: (0,0,0) Value: 10
# Index: (0,0,1) Value: 20
# Index: (0,0,2) Value: 30
# ...
# Index: (1,1,2) Value: 120

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
]
)

for idx,val in np.ndenumerate(arr):
    print(idx,val)

