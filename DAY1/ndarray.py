# ndarray

        # ndarray means N-dimensional Array

        # ndarray is a special data structure 
        # used to store numerical data efficiently.

        # N = Any number
        # 1 Dimension
        # 2 Dimension
        # 3 Dimension
        # 7 Dimension
        # 8 Dimension
        # 10 Dimension
        # 100 Dimension
        # 200 Dimension


        # ndarray store same data type so it is fast

        # IMP RULE  

                # All element should have same datatype

                # [10,20,30]
                # [10.5,20.4,30.6]
                # ["A","B","C"]

            # [10,"Rahul",True]

            # then numpy automatically covert to same data type

import numpy as np

a=np.array([10,20.5,30])

# Output

# array([10. ,20.5,30. ])

# Numpy covert all element in same data type because it required same data type

# Python List

[10,20,30]

# numpy list
# array([10,20,30])

# -----------------------------------------------------------------------------------------

# Dimensions (ndim)

# it means how many indexs is need to acces dataa


# 1D Array

    # 1D array means one dimension aaray
    # it has only one row
    # 1D means 1 index
    # a[0]


# Example:- 

import numpy as np

a=np.array([1,2,3,4,5])
print(a.ndim)

# output

# 1 -- Because it has only one row

# like, Marks - 90,87,68,97,68,87
# like, salary - 96000,80000,68000,97000,68000,87000
# like, age - 19,17,28,37,28,17

# This is one dimesion example

# --------------------------------------------------------------

# 2D Array

        # 2d array means it has rows and column
        # 2D means 2 index
        # a[1][2]

# Example:- 

a=np.array([
    [10,20,30],
    [40,50,60]
])       

print(a.ndim)


# 3D Array

        # A 3D array is an array that contains multiple 2D arrays.
        # 3D means 3 index
        # a[0][1][1]
        # 3D means BOX - Length, Width, Height

a=np.array([
[[1,2],[3,4]], 
[[5,6],[7,8]]
])
print(a.ndim)
print(a.shape)

# ------------------------------------------------------------

# Important Functions

    # a.ndim

        # Number of dimensions

    # a.shape  -- Structure of the Array

        # Number of rows/columns in each dimension

import numpy as np

a = np.array([10,20,30,40])
print(a.shape)

b=np.array([
[1,2,3],
[4,5,6]
])
print(b.shape)

c=np.array([
[
[1,2],
[3,4]
],

[
[5,6],
[7,8]
]
])

print(c.shape)

# Output

# (2,2,2)

# means

# 2 Layers
# 2 Rows
# 2 Column

# --------------------------------------------------------

    # a.size

        # Total elements in array

a=np.array([10,12,14,16])
print(a.size)

# output 4

a=np.array([
    [10,20,30],
    [40,50,60]
])

# Output 6

a=np.array([
[
[1,2],
[3,4]
],

[
[5,6],
[7,8]
]
])

# Output 8

import numpy as np

a=np.array([10,12,14,16])
print(a)
print(a.ndim)
print(a.size)
print(a.shape)
import numpy as np
b=np.array(
    [
    [10,12,14,16,12],
    [11,21,31,24,34]
    ])
print(b)
print(b.ndim)
print(b.size)
print(b.shape)


# --------------------------------------------------------------------------- 

# dtype (Data Type)

    # dtype tells us what type of data is stored inside the NumPy array.

a = np.array([10,20,30])
print(a.dtype)

a=np.array([10.5,20.3,30.8])
print(a.dtype)

a=np.array(["Rahul","Amit","Rohan"])
print(a.dtype)

# mixed 

a=np.array([10,20.5,30])

print(a)
print(a.dtype)

# Automatic Conversion

    # NumPy automatically converts smaller datatype into a larger compatible datatype.

# -------------------------------------------------------------------------------------------------

# itemsize

        # itemsize returns the memory (in bytes) occupied by ONE element of the array.

        # Memory per element -- 8 Bytes

# 1 Byte = 8 Bits

# 1024 Bytes = 1 KB

# 1024 KB = 1 MB

# 1024 MB = 1 GB

a=np.array([10,20,30,],dtype=np.int64)
print(a.itemsize)

# Output 8 

a=np.array([10,20,30,],dtype=np.int32)
print(a.itemsize)

# output 4 

a=np.array([10,20,30,],dtype=np.int16)
print(a.itemsize)

# Output 2

a=np.array([10,20,30,],dtype=np.int8)
print(a.itemsize)

# Output 1

# --------------------------------------------------------------------------

# nbytes

        # Total memory of array
        # nbytes returns the total number of bytes occupied by all elements in the array.

        # nbytes = size * itemsize


# -------------------------------------------------------------

# Arrays vs Python Lists

# | Feature                 | Python List         | NumPy Array         |
# | ----------------------- | ------------------- | ------------------- |
# | Purpose                 | General Programming | Numerical Computing |
# | Speed                   | Slow                | Very Fast           |
# | Memory                  | High                | Low                 |
# | Datatype                | Mixed               | Same Type           |
# | Mathematical Operations | Manual Loop         | Direct              |
# | Best For                | General Data        | Numbers             |
