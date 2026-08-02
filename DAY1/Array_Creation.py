# Creating NumPy Arrays


# ARRAY CREATION

"""
WHAT IS ARRAY CREATION?

Array Creation means creating a NumPy ndarray object.

Before performing any mathematical operation,
NumPy first needs an array to store the data.

Without creating an array,
NumPy cannot perform calculations.

PostgreSQL Analogy

CREATE TABLE
      ↓
INSERT DATA
      ↓
SELECT DATA

NumPy Analogy

Create Array
      ↓
Store Values
      ↓
Perform Calculations
"""

"""
                    ARRAY CREATION
        ┌──────────────────┼──────────────────┐
 Existing Data      Default Values     Generate Values
        │                  │                  │
 array()             zeros()            arange()
 asarray()           ones()             linspace()
 copy()              empty()            logspace()
                     full()             geomspace()
                     eye()
                     identity()
"""

# ==========================================================
# CATEGORY 1 : EXISTING DATA
# ==========================================================

"""
CATEGORY 1 : EXISTING DATA

        Use these functions when you already have data
        and want to convert it into a NumPy ndarray.

    Examples of Existing Data

        • Python List
        • Tuple
        • Range
        • Nested List
        • Another ndarray

    Functions

        1. np.array()
        2. np.asarray()
        3. np.copy()
"""

# ==========================================================
# np.array()
# ==========================================================

    # It converts existing Python data into a NumPy ndarray.

import numpy as np

marks=[80,70,90,97]

arr=np.array(marks)
print(arr)


# ==========================================================
# np.asarray()
# ==========================================================

    # It also converts data into ndarray.

    # Special Rule

        # If the input is already an ndarray,
        # it DOES NOT create another array.

        # Instead,

        # it reuses the existing array.
        # instead of creating another one.
        # This saves memory.

import numpy as np

arr1=np.array([111,222,333,444])

arr2=np.asarray(arr1)

print(arr2)

print(arr2 is arr1)

# ==========================================================
# np.copy()
# ==========================================================

    # It creates a completely independent copy of an array.
    # A new memory location is created.
    # Changing one array does not affect the other.

arr1=np.array([101,102,103,104,105])

arr2=np.copy(arr1)

print(arr2)

arr2[0]=999

print(arr1)
print(arr2)

# Notice new array as it is no any changig effect on orignial array
# orginail array is safe


# ==========================================================
# CATEGORY 2 : DEFAULT VALUES
# ==========================================================


"""
        Use these functions when you DON'T have data yet,
        but you know the size (shape) of the array.

        NumPy automatically creates the array
        and fills it with default values.

        Examples

        Need 5 values

        ↓

        NumPy can automatically create

        0 0 0 0 0

        or

        1 1 1 1 1

        or

        99 99 99 99 99

        or

        Identity Matrix

Functions

        1. np.zeros()
        2. np.ones()
        3. np.empty()
        4. np.full()
        5. np.eye()
        6. np.identity()
"""

# ==========================================================
# np.zeros()
# ==========================================================

    
    # Creates a new array where
    # every element is 0.

import numpy as np

arr = np.zeros(5)

print(arr)

# ==========================================================
# np.ones()
# ==========================================================

    # Creates an array where
    # every value is 1.

import numpy as np

demo=np.ones(5)
print(demo)


# ==========================================================
# np.empty()
# ==========================================================

    # Creates an array without
    # initializing the values.

    # Memory is allocated,

    # but NumPy DOES NOT fill it.

    # The array contains
    # whatever data already exists
    # in that memory location.

    # These are called

    # Garbage Values.

import numpy as np

demo=np.empty(5)
print(demo)

# Output 

# [2.12199579e-314 4.27242889e+180 5.28555900e+180 8.40736310e-315 0.00000000e+000]


# ==========================================================
# np.full()
# ==========================================================

    # Creates an array where
    # every element has
    # the same value.

import numpy as np

demo=np.full(5,99)
print(demo)


# ==========================================================
# np.eye()
# ==========================================================

    # Creates an Identity Matrix.

    # Can create both

    # Square and Rectangular

    # identity-like matrices.

    # Diagonal = 1

    # Everything else = 0

    # It can create rectangular matrices.

    # Returns

    # 2D NumPy ndarray.

import numpy as np

demo=np.eye(5)
print(demo)

# it is used in 

    # Machine learning
    # Deep learning
    # Matrix Multiplixation 
    # Linear Algebra

# ==========================================================
# np.identity()
# ==========================================================

# Also creates an Identity Matrix.

# Only creates square identity matrices.

# Very similar to np.eye(). but Only output has one extra [] bracket

# Returns

# 2D NumPy ndarray.

import numpy as np

demo=np.identity(5)
print(demo)


# ==========================================================
# CATEGORY 3 : GENERATED VALUES
# ==========================================================


    # Use these functions when you DO NOT have data,
    # and you want NumPy to generate the values automatically.


    # Then

        # arange() -- 1 2 3 4 5 ...

        # linspace() -- 0 25 50 75 100

        # logspace() -- 1 10 100 1000

        # geomspace() -- 2 4 8 16 32

# ==========================================================
# np.arange()
# ==========================================================


    # Creates an array with evenly spaced values
    # using a fixed step size.

    # it is similar like Python range().

import numpy as np

arr = np.arange(1,11)
arr1 = np.arange(1,21,2)

print(arr)
print(arr1)

# ==========================================================
# np.linspace()
# ==========================================================

    # Creates equally spaced values
    # between a start and an end value.

    # Start
    # End
    # Number of values

    # NumPy automatically calculates
    # the spacing.

import numpy as np

arr = np.linspace(0,100,6)

print(arr)

# ==========================================================
# np.logspace()
# ==========================================================

    # It creates numbers using powers.
    
    # Creates numbers that are evenly spaced
    # on a logarithmic scale.

    # Instead of adding values,
    # the numbers grow by powers of a base.

    # Default Base = 10

import numpy as np

arr = np.logspace(0,3,4)

print(arr)

"""
So NumPy generated

        10⁰

        10¹

        10²

        10³

Now calculate

        10⁰ = 1

        10¹ = 10

        10² = 100

        10³ = 1000

Final Output

        1

        10

        100

        1000
"""

# Another Example

arr = np.logspace(1,4,4)

print(arr)

# Start power

# 10¹

# End power

# 10⁴

# ==========================================================
# np.geomspace()
# ==========================================================

    # Creates values that form
    # a geometric progression.

    # Each value is multiplied
    # by a constant ratio.

import numpy as np

arr = np.geomspace(1,1000,4)

print(arr)

"""

Output

[   1.   10.  100. 1000.]

Another Example

arr = np.geomspace(2,16,4)

print(arr)

Output

[ 2.  4.  8. 16.]

Notice

2 * 2 = 4

4 * 2 = 8

8 * 2 = 16

Each number is multiplied by the same ratio.

"""