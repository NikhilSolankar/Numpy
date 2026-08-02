# next chapter 2
# numpay properties
# mathamatical operation

import numpy as np

# shape
# shape help to find How many Rows and cloumns in your array/ matrix

arr_2d=np.array([[1,2,3],
                [4,5,6]])
print(arr_2d.shape)

# it return (2,3)

# size

# it return the size of array
# total number of elements in array

array_2d=np.array([[1,2,3],
                [4,5,6]])

print(array_2d.size)
# return 6

arra_2d=np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arra_2d.size)
# return 9

# ndim
# it return number of dimension

arra_d=np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arra_d.ndim)

arra_d1=np.array([[[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12]]])
print(arra_d1.ndim)

# bracket matter for dimension ? 1 dimension -[] , 2- [[]],3 - [[[]]]?

#next
#.dtype
# data type if elements
#int,float,string

arrdemo=np.array([1,2,3,4,5,6])
print(arrdemo.dtype)


arrdemo1=np.array([1,2,3,4,5,6,4.3])
print(arrdemo1.dtype)


arrdemo2=np.array([1,2,3,4,5,6,3.34,'String'])
print(arrdemo2.dtype)

# astype()
# convert one datype to another

asdemo=np.array([12,23,45])
print(asdemo.astype(str))

asdemo1=np.array([12,23,45])
print(asdemo1.astype(float))

asdemo2=np.array([1.2,2.3,4.5])
print(asdemo2.astype(int))


# Mathamatical Operation
# + - * / ** %
arr1=np.array([10,20,30,40,50])
print(arr1)
print(arr1 + 5)
print(arr1 - 2)
print(arr1 * 5)
print(arr1 ** 2)
print(arr1 / 2)

# Aggregation function

# sum(), mean(), max(), min(), std() -- Standard daviation, var() -- variacnce

arr2=np.array([10,20,30,40,50])

print(np.sum(arr2))
print(np.mean(arr2))
print(np.max(arr2))
print(np.min(arr2))
print(np.std(arr2))
print(np.var(arr2))

