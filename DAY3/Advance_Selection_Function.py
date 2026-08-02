# ADVANCED SELECTION FUNCTIONS

	# where()
	# nonzero()	
	# argwhere()
	# take()
	# put()
	# compress()
	# choose()
	# extract()
	# select()

# These functions help us select, find, replace,
# and manipulate elements in an array

# Where()

        # where() checks a condition.

        # If the condition is True,

        # it returns the index of that element.

        # It can also replace values
        # using True and False conditions

        # syntax

            # res=np.where(arr>20)

        # Replace Value Syantax

            # result=np.where(arr>40,100,0)

# Example:- 

# Find index of numbers greater than 30

import numpy as np

arr=np.array([10,20,30,40,50])

result=np.where(arr>30)
print(result)

# replace Value

res=np.where(arr>30,100,0)
print(res)

# if condition is true then replace by 100 
# if conditon is false then replace by 0

# Example:- 

# student Marks

marks=np.array([45,70,80,30,95])

result=np.where(marks>=40,"Pass","Fail")
print(result)

# --------------------------------------------------------------------

# nonzero()

        # Returns the indexes of all non-zero elements.
        # Syntax

            # np.nonzero(arr)
        
arr=np.array([5,24,0,2,1,0,0.0,2,1,3,5,0,2,11])
print(np.nonzero(arr))

# Output

# (array([ 0,  1,  3,  4,  7,  8,  9, 10, 12, 13]),)

# index 2 skip because elemenet is 0
# index 5 skip because element is 0

print()
arr=np.array([
    [0,10,20,1,0],
    [1,0,2,20,0]
])
print(np.nonzero(arr))

# ----------------------------------------------------------------

# argwhere()

        # it return row and column position of elements
        # that satisfy a conditon 

arr=np.array([
    [10,20,30,40],
    [20,10,40,30],
    [30,10,40,20],
])

print(np.argwhere(arr>30))

# Output

# [[0 3]
# [1 2]
# [2 2]]

# differenec
# Where () return the actual element 
# arswhere() return the position of element (index number)

# ------------------------------------------------------------------------

# take()

        # Select elements using indexes.
        # Similar to Fancy Indexing.

        # Syntax:- 
        # no.take(arr,indexs)

# Example:- 

arr=np.array([10,20,30,40,50,60,70,80,90,100])

print(np.take(arr,5))
print(np.take(arr,[4,5]))
print(np.take(arr,[5,1,7,2]))

arr=np.array([
    [10,20],
    [30,40],
])

print(np.take(arr,[1,0]))
print(np.take(arr,[1,3]))

arr=np.array([
    [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]
])
print()
print(np.take(arr,[0,3]))
print(np.take(arr,[2,1]))
print(np.take(arr,8))

# Numpy first flatten the array
# and assign index number to each elements

# --------------------------------------------------------------------------

# put()

        # Replaces values at given indexes.

        # Syntax

                # np.put(arr,indexes,values)
            
arr=np.array([10,20,30,40,50])

np.put(arr,2,100)
print(arr)

np.put(arr,[0,4],[201,501])
print(arr)

# -----------------------------------------------------------------------

# compress()

        # Select elements using a Boolean mask.
        # which element value is true then keep this element 
        # remove element whos values is false

arr=np.array([10,20,30,40,50])
mask=[True,False,True,False,True]
print(np.compress(mask,arr))

# Output

# [10 30 50]

# -------------------------------------------------------------------------

# Choose()

        # Select values from multiple arrays
        # based on index choices.

        # Syntax 

            # np.choice(choise,[arr1,arr2,.....])
    
choice=np.array([0,1,0,1,0])

a=np.array([10,20,30,40,50])
b=np.array([100,200,300,400,500])

print(np.choose(choice,[a,b]))

# Output [ 10 200  30 400  50]

# Each array assign 0 and 1 value
# means

#              0, 1, 0, 1, 0
# a=np.array([10,20,30,40,50])

#              0,  1,  0,  1,  0
# b=np.array([100,200,300,400,500])

# 0 take from a
# 1 take from b
# 0 take from a
# 1 take from b

# ---------------------------------------------------------------

# extract()

        # Returns elements that satisfy a condition.
        # return exact value

        # Syntax
        # np.extract(condition,array)
    
arr=np.array([10,20,30,40,50,60,70,80,90,100])
print(np.extract(arr>50,arr))

# Output
# [ 60  70  80  90 100]

# Difference

# where()

# returns indexes

# extract()

# returns values

# argwhere()
# it return row and column position

# ------------------------------------------------------------------------

# select()

        # Checks multiple conditions
        # and returns different values
        # for each condition.

        # it like multiple if-elif-else statements.

        # Syntax
            # np.select(condition_list, choice_list, default)

marks=np.array([30,55,65,60,90,32,72,98])

conditions=[
    marks<40,
    marks<50,
    marks<70,
    marks<90,
    marks<100
]

choices=[
    "Fail",
    "Pass",
    "Good",
    "Very Good",
    "Excellent"
]

result=np.select(conditions,choices,"None")
print(result)

# ---------------------------------------------------------------------------

# Q1 Create the following array.

# [10,20,30,40,50]

# Using np.where()

# Find the indexes
# where value > 30.

# Expected Output

# (array([3,4]),)


# ----------------------------------------------------------


# Q2 Create the following array.

# [5,0,10,0,20,30]

# Using np.nonzero()

# Print the indexes
# of all non-zero elements.

# Expected Output

# (array([0,2,4,5]),)


# ----------------------------------------------------------


# Q3 Create the following array.

"""
[
 [10,20],
 [30,40]
]
"""

# Using np.argwhere()

# Find the positions
# where value > 20.

# Expected Output

# [[1 0]
#  [1 1]]


# ----------------------------------------------------------


# Q4 Create the following array.

# [100,200,300,400,500]

# Using np.take()

# Print

# [100 300 500]


# ----------------------------------------------------------


# Q5 Create the following array.

# [10,20,30,40]

# Using np.put()

# Replace

# 20 → 200
# 40 → 400

# Print the updated array.


# ==========================================================
# INTERMEDIATE LEVEL (Q6 - Q10)
# ==========================================================

# Q6 Create the following array.

# [10,20,30,40,50]

# Using np.where()

# Replace

# values >30 with 100

# otherwise replace with 0

# Expected Output

# [0 0 0 100 100]


# ----------------------------------------------------------


# Q7 Create the following array.

# [10,20,30,40,50]

# Create the following mask.

# [True,False,True,False,True]

# Using np.compress()

# Print

# [10 30 50]


# ----------------------------------------------------------


# Q8 Create two arrays.

# arr1

# [10,20,30,40]

# arr2

# [100,200,300,400]

# choice

# [0,1,0,1]

# Using np.choose()

# Print

# [10 200 30 400]


# ----------------------------------------------------------


# Q9 Create the following array.

# [5,10,15,20,25,30]

# Using np.extract()

# Extract all values
# greater than 15.

# Expected Output

# [20 25 30]


# ----------------------------------------------------------


# Q10 Create the following array.

# [30,55,72,90]

# Using np.select()

# Conditions

# marks <40

# marks <75

# marks >=75

# Choices

# "Fail"

# "Pass"

# "Excellent"

# Expected Output

# ['Fail' 'Pass' 'Pass' 'Excellent']


# ==========================================================
# ADVANCED LEVEL (Q11 - Q15)
# ==========================================================

# Q11 Create the following array.

"""
[
 [10,20,30],
 [40,50,60],
 [70,80,90]
]
"""

# Using np.argwhere()

# Find all positions
# where value >=50.


# ----------------------------------------------------------


# Q12 Create the following array.

"""
[
 [0,10,0],
 [20,30,0]
]
"""

# Using np.nonzero()

# Print the row indexes
# and column indexes
# of all non-zero elements.


# ----------------------------------------------------------


# Q13 Create the following array.

# [10,20,30,40,50]

# Using np.put()

# Replace

# index 0 → 999

# index 4 → 888

# Print the updated array.


# ----------------------------------------------------------


# Q14 Create the following array.

"""
[
 [10,20],
 [30,40]
]
"""

# Using np.take()

# Print

# [10 40]

# Hint

# Remember

# np.take()

# first flattens
# the array.


# ----------------------------------------------------------


# Q15 ⭐ Challenge

# Create the following array.

# [25,40,60,75,90]

# Using np.select()

# Apply the following conditions.

# marks <35

# marks <60

# marks <80

# marks >=80

# Choices

# "Fail"

# "Pass"

# "Good"

# "Excellent"

# Expected Output

# ['Fail'
#  'Pass'
#  'Good'
#  'Good'
#  'Excellent']


# ==========================================================
# BONUS INTERVIEW QUESTIONS (Q16 - Q20)
# ==========================================================

# Q16 Predict the Output.

# import numpy as np
#
# arr=np.array([10,20,30,40])
#
# print(np.where(arr>=30))


# ----------------------------------------------------------


# Q17 Predict the Output.

# import numpy as np
#
# arr=np.array([0,5,0,10])
#
# print(np.nonzero(arr))


# ----------------------------------------------------------


# Q18 Predict the Output.

# import numpy as np
#
# arr=np.array([
#     [10,20],
#     [30,40]
# ])
#
# print(np.argwhere(arr>15))


# ----------------------------------------------------------


# Q19 Predict the Output.

# import numpy as np
#
# arr=np.array([10,20,30,40])
#
# print(np.extract(arr>20,arr))


# ----------------------------------------------------------


# Q20 ⭐⭐⭐ Predict the Output.

# import numpy as np
#
# arr=np.array([10,20,30,40])
#
# result=np.where(arr>20,1,0)
#
# print(result)