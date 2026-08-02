# Joining Arrays

        # Joining Arrays means combining two or more arrays into a single array.

        # Instead of creating a new array manually, 
        # NumPy provides several functions to join arrays in different ways.

        # Joining arrays is useful when:
                
                # Combining multiple datasets
                # Merging training data in Machine Learning
                # Combining rows or columns
                # Processing large datasets
                # Preparing data for AI and Deep Learning

# Types of Joining Arrays


    # concatenate()
    # stack()
    # vstack()
    # hstack()
    # dstack()
    # row_stack()
    # column_stack()

# -----------------------------------------------
# axis=0 → Arrays are joined row-wise (one below another).
# axis=1 → Arrays are joined column-wise (one beside another).
# -----------------------------------------------------

# concatenate()

        # concatenate() joins two or more arrays along an existing axis.
        # It does not create a new axis.
        # It simply connects arrays together.

import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])

result=np.concatenate((arr1,arr2))
print(result)

# Output [ 1  2  3  4  5  6  7  8  9 10]

arr1 = np.array([
    [1,2],
    [3,4]
])

arr2 = np.array([
    [5,6],
    [7,8]
])

new = np.concatenate((arr1,arr2), axis=0)

print(new)

# Output

# [[1 2]
# [3 4]
# [5 6]
# [7 8]]

print("------------- Using Axis = 1 -------------------")
arr1 = np.array([
    [1,2],
    [3,4]
])

arr2 = np.array([
    [5,6],
    [7,8]
])

new = np.concatenate((arr1,arr2), axis=1)

print(new)

# Output 

# [[1 2 5 6]
# [3 4 7 8]]
# ------------------------------------------------------------------

# stack()

        # stack() joins arrays by creating a new axis.
        # Add one extra dimension

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])

result=np.stack((arr1,arr2,),axis=0)
print(result)   

# Output 
# [[ 1  2  3  4  5]
# [ 6  7  8  9 10]]

# ---------------------------------------------------------------------------

# vstack()

        # vstack() means Vertical Stack.

        # It joins arrays from top to bottom.

        # Rows increase.
    
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
arr3=np.array([11,12,13,14,15])
arr4=np.array([16,17,18,19,20])


result=np.vstack((arr1,arr2,arr3,arr4))
print(result)  

# ------------------------------------------------------

# hstack()

        # hstack() means Horizontal Stack.

        # It joins arrays from left to right.

        # Columns increase.

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
arr3=np.array([11,12,13,14,15])
arr4=np.array([16,17,18,19,20])

result=np.hstack((arr1,arr2,arr3,arr4))
print(result)

# ---------------------------------------------------------------------

# dstack() 

    # dstack() means Depth Stack.

    # It joins arrays along the third dimension (depth).

    # Mainly used with 3D arrays.

import numpy as np

arr1 = np.array([[1,2],
                 [3,4]])

arr2 = np.array([[5,6],
                 [7,8]])

result = np.dstack((arr1, arr2))

print(result)

# --------------------------------------------------------------

# row_stack()

        # row_stack() joins arrays row by row.
        # It behaves almost the same as vstack().
        # You can think of it as another name (alias) for vstack().

    
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
arr3=np.array([11,12,13,14,15])
arr4=np.array([16,17,18,19,20])


result=np.row_stack((arr1,arr2,arr3,arr4))
print(result)  

# --------------------------------------------------------

# column_stack()

        # column_stack() joins arrays column by column.
        # For 1D arrays, NumPy first converts each array into a column and then joins them.

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
arr3=np.array([11,12,13,14,15])
arr4=np.array([16,17,18,19,20])


result=np.column_stack((arr1,arr2,arr3,arr4))
print(result)         

print("-----------------------------------------------------------------------")


# Q1 Create two 1D arrays and join them using concatenate().

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

result=np.concatenate((arr1,arr2))
print(result)
print()
# Q2 Join two (2,2) arrays using concatenate(axis=0).
arr1=np.array([     
                [1,2],
                [3,4]     
])
arr2=np.array([
        [5,6],
        [7,8],

])

result=np.concatenate((arr1,arr2),axis=0)
print(result)
print()
# Q3 Join the same arrays using concatenate(axis=1).

arr1=np.array([     
                [1,2],
                [3,4]     
])
arr2=np.array([
        [5,6],
        [7,8],

])

result=np.concatenate((arr1,arr2),axis=1)
print(result)
print()

# Q4 Join two 1D arrays using stack().

arr1=np.array([11,12,13,14])
arr2=np.array([21,22,23,24])

result=np.stack((arr1,arr2))
print(result)
print()

# Q5 Join the same arrays using:

# axis=0
# axis=1

arr1=np.array([11,12,13,14])
arr2=np.array([21,22,23,24])

result1=np.stack((arr1,arr2),axis=0)
print(result1)
print()

arr1=np.array([11,12,13,14])
arr2=np.array([21,22,23,24])

result2=np.stack((arr1,arr2),axis=1)
print(result2)
print()

# Print the shapes.
print(result1.shape)
print(result2.shape)
print()

# Q6 Use vstack() to join four 1D arrays.

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr3=np.array([9,10,11,12])
arr4=np.array([13,14,15,16])

result=np.vstack((arr1,arr2,arr3,arr4))
print(result)

# Q7 Use hstack() to join four 1D arrays.

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr3=np.array([9,10,11,12])
arr4=np.array([13,14,15,16])

result=np.hstack((arr1,arr2,arr3,arr4))
print(result)

# Q8 Use row_stack().

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr3=np.array([9,10,11,12])
arr4=np.array([13,14,15,16])

result=np.row_stack((arr1,arr2,arr3,arr4))
print(result)

# Compare the result with vstack().

# vstack() and row_stack return same result

# Q9 Use column_stack() on three 1D arrays.

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr3=np.array([9,10,11,12])

result=np.column_stack((arr1,arr2,arr3))
print(result)

# Print the output.

# [[ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]
#  [ 4  8 12]]
 
# Q10 Use dstack() on two (2,2) arrays.

arr1=np.array([
        [1,2],
        [3,4]
])


arr2=np.array([
        [5,6],
        [7,8]
])

res=np.dstack((arr1,arr2))
print(res)

# Print:
# Array
# Shape
print(res.shape)
print()

# Q11 Create two (2,3) arrays.

arr1=np.array(
        [
                [11,12,13],
                [14,15,16],

        ]
)

arr2=np.array(
        [
                [21,22,23],
                [24,25,26],

        ]
)


# Join them using:

# concatenate(axis=0)

res=np.concatenate((arr1,arr2),axis=0)
print(res)

# concatenate(axis=1)

res1=np.concatenate((arr1,arr2),axis=1)
print(res1)

# stack(axis=0)

res2=np.stack((arr1,arr2),axis=0)
print(res2)

# stack(axis=1)

res3=np.stack((arr1,arr2),axis=1)
print(res3)

# Compare every shape.
print(res.shape)
print(res1.shape)
print(res2.shape)
print(res3.shape)

# Q12 Create three (3,3) arrays.

arr1=np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9],
])

arr2=np.array([
        [11,12,13],
        [14,15,16],
        [17,18,19],
])

arr3=np.array([
        [21,22,23],
        [24,25,26],
        [27,28,29],
])
print(arr1)
print(arr2)
print(arr3)
print()
# Join them using:

# stack()
res1=np.stack((arr1,arr2,arr3))
print(res1)
print()

# vstack()
res2=np.vstack((arr1,arr2,arr3))
print(res2)
print()

# hstack()

res3=np.hstack((arr1,arr2,arr3))
print(res3)

# Print the shape after each operation.
print(res1.shape)
print(res2.shape)
print(res3.shape)

# Q13 Create three (2,2) arrays.

ar1=np.array([
        [1,2],
        [3,4],
])

ar2=np.array([
        [5,6],
        [7,8],
])


ar3=np.array([
        [9,10],
        [11,12],
])

# Join them using dstack().

res=np.dstack((ar1,ar2,ar3))
print(res)

# Print the resulting shape.
print(res.shape)

# Q14 Create four arrays.

array1=np.array([1,2,3,4,5])
array2=np.array([6,7,8,9,10])
array3=np.array([11,12,13,14,15])
array4=np.array([16,17,18,19,20])

# Use:

# concatenate()

res=np.concatenate((array1,array2,array3,array4))
print(res)

# stack()
res=np.stack((array1,array2,array3,array4))
print(res)

# vstack()
res=np.vstack((array1,array2,array3,array4))
print(res)

# hstack()
res=np.hstack((array1,array2,array3,array4))
print(res)

# row_stack()
res=np.row_stack((array1,array2,array3,array4))
print(res)

# column_stack()
res=np.column_stack((array1,array2,array3,array4))
print(res)

# Print every result.

# Q15 Create five arrays of shape (2,2).
array1=np.array([
        [1,2],
        [3,4],
])

array2=np.array([
        [5,6],
        [7,8],
])

array3=np.array([
        [9,10],
        [11,12],
])

array4=np.array([
        [13,14],
        [15,16],
])

array5=np.array([
        [17,18],
        [19,20],
])

# Use every joining function:

# concatenate()
res1=np.concatenate((array1,array2,array3,array4))
print(res1)

# stack()
res2=np.stack((array1,array2,array3,array4))
print(res2)

# vstack()
res3=np.vstack((array1,array2,array3,array4))
print(res3)

# hstack()
res4=np.hstack((array1,array2,array3,array4))
print(res4)

# dstack()
res5=np.dstack((array1,array2,array3,array4))
print(res5)

# row_stack()
res6=np.row_stack((array1,array2,array3,array4))
print(res6)

# column_stack()
res7=np.column_stack((array1,array2,array3,array4))
print(res7)

# Print:

# Output
# Shape
print(res1.shape)
print(res2.shape)
print(res3.shape)
print(res4.shape)
print(res5.shape)
print(res6.shape)
print(res7.shape)

