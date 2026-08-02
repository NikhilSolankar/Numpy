# LEVEL 1 : BEGINNER (1-20)

# Array Creation

# Q1  Create a NumPy array containing

# 10 20 30 40 50

import numpy as np

arr=np.array([10,20,30,40,50])
print(arr)

# Q2 Create an array from the tuple

# (5,10,15,20)

data=(5,10,15,20)

arr=np.array(data)
print(arr)

# Q3 Create a NumPy array from

# range(1,11)

ran=np.array(range(1,11))
print(ran)

# Q4 Create a 1D array containing

# 100
# 200
# 300
# 400
# 500

arr=np.array([100,200,300,400,500])
print(arr)
print(arr.ndim)

# Q5 Create a 2×3 array

# 1 2 3

# 4 5 6

arr=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr)


# Default Values

# Q6 Create an array of 5 zeros.

arr=np.zeros(5)
print(arr)

# Q7 Create an array of 10 ones.

arr=np.ones(10)
print(arr)

# Q8 Create an array of 8 values filled with 99

arr=np.full(8,99)
print(arr)

# Q9 Create a 3×3 identity matrix.

arr=np.eye(3)

print(arr)

# Q10 Create an empty array of size 5 

arr=np.empty(5)
print(arr)

# Print the output.

# [0. 0. 0. 0. 0.]

# Generated Values

# Q11 Generate numbers 1 to 20.

arr=np.arange(1,21)
print(arr)

# Q12 Generate even numbers between 2 and 20.

arr=np.arange(2,21,2)
print(arr)

# Q13 Generate odd numbers between 1 and 19.

arr=np.arange(1,20,2)
print(arr)


# Q14 Generate 5 equally spaced values between 0 and 100.

arr=np.linspace(0,100,5)
print(arr)

# Q15 Generate

# 1

# 10

# 100

# 1000

# using

# np.logspace().

arr=np.logspace(0,3,4)
print(arr)

# Q16

# Generate

# 2

# 4

# 8

# 16
 
# using

# np.geomspace().

arr=np.geomspace(2,16,4)
print(arr)


# Array Information

# Use this array

# arr=np.array([[10,20,30],[40,50,60]])

# Q17 Print the array.

arr=np.array(
    [
        [10,20,30],
        [40,50,60]
        
    ])

print(arr)

# Q18 Print Shape 
arr=np.array(
    [
        [10,20,30],
        [40,50,60]
        
    ])

print(arr.shape)

# Q19 Print Dimensions

arr=np.array(
    [
        [10,20,30],
        [40,50,60]
        
    ])

print(arr.ndim)

# Q20 Print Size

arr=np.array(
    [
        [10,20,30],
        [40,50,60]
        
    ])

print(arr.size)


# -------------------------------------------------------------------------------
print("----------------------------------------------------")
# INTERMEDIATE LEVEL (10 QUESTIONS)

# ==========================================================
# Q1. Existing Data Conversion
# ==========================================================

# Convert the following Python List into a NumPy array
# WITHOUT changing the original list.

marks = [85, 92, 78, 96, 88]

# Then print:
# 1. The array
# 2. Shape
# 3. Size
# 4. dtype

marks = [85, 92, 78, 96, 88]

arr=np.array(marks)
print(arr)
print(arr.shape)
print(arr.size)
print(arr.dtype)

# ==========================================================
# Q2. array() vs asarray()
# ==========================================================

# Write a program to prove that

# 1. np.array() creates a NEW array.
# 2. np.asarray() reuses an existing NumPy array whenever possible.

# Use the "is" operator to verify your answer.

# Print the results.

arr=[10,20,30,40,50]

res=np.array(arr)
res1=np.asarray(res)

print(res is res1)
print(res1 is res)


# ==========================================================
# Q3. copy()
# ==========================================================

# Create
# arr1 = np.array([100,200,300,400])

# Now

# 1. Create arr2 using np.copy()
# 2. Change the second element of arr2 to 999
# 3. Print arr1
# 4. Print arr2
# 5. Explain why arr1 did not change.

arr1 = np.array([100,200,300,400])

arr2=np.copy(arr1)

arr2[1]=999

print(arr1)
print(arr2)

# arr1 is not change because it is orginal array and we copay arr1 aaray to arr2 and perform operation on arr2 so arr one is safe

# ==========================================================
# Q4. Default Value Functions
# ==========================================================

# Without writing the numbers manually,
# create the following arrays.

# a)

# 0 0 0 0 0

arr=np.zeros(5)
print(arr)

# b)

# 1 1 1 1 1

arr=np.ones(5)
print(arr)

# c)

# 50 50 50 50 50

arr=np.full(5,50)
print(arr)

# ==========================================================
# Q5. Number Generation
# ==========================================================

# Generate the following arrays.

# a)

# 5 10 15 20 25 30

arr=np.arange(5,35,5)
print(arr)

# b)

# 100 90 80 70 60 50

arr=np.arange(100,40,-10)
print(arr)

# Hint:
# Think carefully about the step value.


# ==========================================================
# Q6. linspace()
# ==========================================================

# Generate exactly 11 equally spaced values
# between 0 and 100.

arr=np.linspace(0,100,11)
print(arr)

# Then answer

# 1. How many values are there?
# There are 11 values are there 

# 2. What is the difference (gap)
#  between consecutive values? ans 10


# ==========================================================
# Q7. Identity Matrix
# ==========================================================

# Create

# 1. A 4 × 4 Identity Matrix.

arr=np.identity(4)
print(arr)

# 2. A 3 × 5 Identity-like Matrix.

arr=np.eye(3,5)
print(arr)

# Then answer

# Which function did you use?

# np.eye() ?

# or

# np.identity() ?

# Explain your answer.

# i use np.eye() beasue it create matrix 

# ==========================================================
# Q8. Memory Calculation
# ==========================================================

# Given

# arr = np.array([10,20,30,40,50,60])

# Without using

# arr.nbytes

# Calculate the total memory used
# by the array.

# Hint

# Use

# size

# and

# itemsize

arr = np.array([10,20,30,40,50,60])

memory = arr.size * arr.itemsize
print(memory)

# ==========================================================
# Q9. Predict the Output
# ==========================================================

# Without running the code,
# predict the output.

"""
import numpy as np

arr = np.array([1,2,3])

arr2 = np.asarray(arr)

arr2[0] = 100

print(arr)

print(arr2)
"""
# Output 
# [100,2,3]
# [100,2,3]

# Then explain

# Why did this happen?

# because asarray or array both point to same


# ==========================================================
# Q10. Mini Challenge
# ==========================================================

# Write a complete program.

# Requirements

# 1. Create a 3 × 3 array filled with 7.

arr=np.full((3,3),7)
print(arr)

# 2. Print

# Shape
print(arr.shape)

# Number of Dimensions
print(arr.ndim)

# Size
print(arr.size)

# Data Type
print(arr.dtype)

# Item Size
print(arr.itemsize)

# Total Memory Used
print(arr.nbytes)


# 3. Create a copy of the array.

cop=np.copy(arr)

# 4. Change ONE value
#    inside the copied array.

cop[0,0]=111


# 5. Print

# Original Array
print(arr)

# Copied Array
print(cop)

# 6. Explain why
#    the original array did not change.

# np.copy() creates a completely independent copy of the original array.

# The copied array has its own memory location.

# Therefore, changing the copied array does not affect the original array because both arrays are stored in different memory locations.

# ==========================================================
# INTERMEDIATE LEVEL - SET 2 (10 QUESTIONS)
# ==========================================================

# ==========================================================
# Q1. Existing Data
# ==========================================================

# Convert the following into a NumPy array.

scores = (45, 67, 89, 91, 76)

# Print

# 1. Array
scores = (45, 67, 89, 91, 76)

arr=np.array(scores)
print(arr)
# 2. Shape
print(arr.shape)
# 3. ndim
print(arr.ndim)
# 4. dtype
print(arr.dtype)


# ==========================================================
# Q2. array() vs copy()
# ==========================================================

# Create

# arr1 = np.array([10,20,30,40])

# Create

# arr2 using np.array(arr1)

arr1 = np.array([10,20,30,40])

arr2 = np.array(arr1)

arr3 = np.copy(arr1)

print(arr1 is arr2)   # False
print(arr1 is arr3)   # False

# Create

# arr3 using np.copy(arr1)

arr3=np.copy(arr2)
print(arr3)
# Print

# arr1 is arr2
# arr1 is arr3

print(arr1 is arr2)
print(arr1 is arr3)


# Modify arr2

arr2[1]=55
print(arr2)

# Modify arr3
arr3[0]=77
print(arr3)

# Print all three arrays.

print(arr1)
print(arr2)
print(arr3)


# ==========================================================
# Q3. Create Different Default Arrays
# ==========================================================

# Create

# a) Five zeros of INTEGER type.

arr=np.zeros(5,dtype=int)
print(arr)

# b) Five ones of FLOAT type.

arr=np.ones(5,dtype=float)
print(arr)

# c) Six values filled with -5.

arr=np.full(6,-5)
print(arr)

# ==========================================================
# Q4. Generate Numbers
# ==========================================================

# Generate

# a) 50 55 60 65 70 75 80

arr=np.arange(50,85,5)
print(arr)

# b) 20 18 16 14 12 10

arr=np.arange(20,8,-2)
print(arr)

# c) 0 5 10 15 20 25

arr=np.arange(0,30,5)
print(arr)

# ==========================================================
# Q5. linspace()
# ==========================================================

# Generate exactly 9 equally spaced values
# between 10 and 90.

arr=np.linspace(10,90,9)
print(arr)

# Then print

# Shape
print(arr.shape)

# Size
print(arr.size)

# Gap between consecutive values.

# ==========================================================
# Q6. logspace() and geomspace()
# ==========================================================

# Generate using logspace()

# 1
# 10
# 100
# 1000
# 10000

arr=np.logspace(0,4,5)
print(arr)

# Generate using geomspace()

# 5
# 10
# 20
# 40
# 80

arr=np.geomspace(5,80,5)
print(arr)
# Explain the difference between both outputs.

# mujee aap haii bataoo kii isamii kayy frkk haii

# ==========================================================
# Q7. Identity Matrix
# ==========================================================

# Create

# a) 6 × 6 Identity Matrix.

arr=np.eye(6)
print(arr)

# b) 4 × 6 Identity-like Matrix.

arr=np.eye(4,6)
print(arr)

# Print both.

# Explain why one uses np.identity()

# and the other uses np.eye().

# aap haii bataoo kii identity and eye kyuu use karuu konaa kabb usee karnaa haii


# ==========================================================
# Q8. Memory Calculation
# ==========================================================

# Create

# arr = np.arange(1,11)

# Print

arr = np.arange(1,11)
print(arr)

# Shape

print(arr.shape)

# Size

print(arr.size)

# Item Size

print(arr.itemsize)

# Total Memory Used

print(arr.nbytes)

# Calculate the total memory manually
# using size and itemsize.


# ==========================================================
# Q9. Predict the Output
# ==========================================================

# Without running the code,
# predict the output.

"""
import numpy as np

arr = np.array([5,10,15])

arr2 = np.copy(arr)

arr2[2] = 999

print(arr)

print(arr2)

print(arr is arr2)
"""

# Explain why.

# Output False

# ==========================================================
# Q10. Mini Challenge
# ==========================================================

# Write a complete program.

# Step 1

# Create a 4 × 4 array
# filled with the value 25.

arr=np.full((4,4),25)
print(arr)

# Step 2

# Print


# Shape
print(arr.shape)

# ndim
print(arr.ndim)

# Size
print(arr.size)

# dtype
print(arr.dtype)

# itemsize
print(arr.itemsize)

# nbytes
print(arr.nbytes)

# Step 3

# Create another array using np.copy().

arr1=np.copy(arr)
print(arr1)

# Step 4

# Change ONLY the center element(s)
# of the copied array to 100.

arr1[1:3,1:3]=100
print(arr1)

# Step 5

# Print

# Original Array
print(arr)
print(arr1)
# Copied Array

# Step 6

# Explain why the original array
# did not change.


# ==========================================================
# END OF INTERMEDIATE SET - 2
# ==========================================================