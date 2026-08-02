# ----------------------------------------------------------
# What is NumPy?
# ----------------------------------------------------------

        # NumPy stands for Numerical Python.

        # Numpay is create by Travis Oliphant in 2005
        
        # NumPy is a powerful Python library used for numerical computing.
        
        # It provides a special data structure called ndarray (N-dimensional Array)
        # to store and process large amounts of numerical data efficiently.

        # NumPy is faster and more memory-efficient than
        # Python Lists for numerical data.
               
        # NumPy is one of the most important libraries in:
        
        # Data Science
        # Machine Learning
        # Deep Learning
        # Artificial Intelligence (AI)
        # Scientific Computing
        # Data Analysis

        # NumPy is the foundation of libraries such as:
        
        #   - Pandas
        #   - SciPy
        #   - Scikit-learn
        #   - TensorFlow
        #   - PyTorch

# ------------------------------------------------------------

# Why Was NumPy Created?


        # Python is a general-purpose programming language.

        # Python Lists can store data, but they are not designed
        # for large-scale numerical calculations.

        # When working with thousands or millions of numbers,
        # Python Lists become slower and use more memory.
        
        # NumPy was created to solve these problems by providing:

            # Faster numerical operations
            # Better memory efficiency
            # Easy mathematical calculations
            # Support for multi-dimensional arrays

# -----------------------------------------------------------------

# Problems with Python Lists


    # Python Lists have some limitations:

        # Slower for large datasets
        # Require more memory
        # Do not support direct element-wise mathematical operations
        # Less suitable for scientific and mathematical computing

# Example

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

# Output
# [1, 2, 3, 4, 5, 6]

# The '+' operator joins (concatenates) the two lists.
# It does NOT add the corresponding elements.

# ----------------------------------------------------------------------------

# How NumPy Solves These Problems

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)

# Output
# [5 7 9]

# NumPy automatically performs element-wise addition.

# ---------------------------------------------------------------------------

# Features of NumPy

        # Fast numerical computations
        # Memory efficient
        # Supports multi-dimensional arrays
        # Easy mathematical operations
        # Large collection of built-in functions
        # Widely used in Data Science and Machine Learning

# --------------------------------------------------------------------

# Applications of NumPy

    # NumPy is widely used in:
        
        # Data Science
        # Machine Learning
        # Deep Learning
        # Artificial Intelligence
        # Data Analysis
        # Scientific Computing
        # Image Processing
        # Signal Processing
        # Financial Analysis
        # Research and Engineering

# -----------------------------------------------------------------------

# Advantages of NumPy

    # Very fast
    # Uses less memory
    # Supports element-wise operations
    # Easy mathematical calculations
    # Excellent support for arrays and matrices
    # Industry standard for numerical computing

# -----------------------------------------------------------------------

# Limitations of NumPy

    # Mainly designed for numerical data
    # Arrays usually contain the same data type
    # Less flexible than Python Lists for storing mixed data

# -----------------------------------------------------------------------

# Python List vs NumPy Array

# Python List

    # Built into Python
    # Slower for numerical operations
    # Uses more memory
    # Stores mixed data types
    # Limited mathematical support

# NumPy Array

    # Provided by NumPy library
    # Faster for numerical operations
    # Uses less memory
    # Best for same data type
    # Powerful mathematical support

# ----------------------------------------------------------

# import NumPy like this:

import numpy as np


# flags

        # The flags attribute provides information about how a NumPy array
        # is stored in memory and whether it can be modified.

        # It is mainly used to inspect the internal properties of an array,
        # such as memory layout, ownership, and write permissions.

arr=np.array([10,20,30])
print(arr.flags)

"""

Sample Output
C_CONTIGUOUS : True
F_CONTIGUOUS : False
OWNDATA : True
WRITEABLE : True
ALIGNED : True
WRITEBACKIFCOPY : False

"""

"""
C_CONTIGUOUS

True → Array is stored in C-style (row-major) contiguous memory.
False → Array is not stored in C-style contiguous memory.

F_CONTIGUOUS

True → Array is stored in Fortran-style (column-major) contiguous memory.
False → Array is not stored in Fortran-style contiguous memory.

OWNDATA

True → The array owns its own memory.
False → The array shares memory with another array (for example, a view).

WRITEABLE

True → Elements of the array can be modified.
False → The array is read-only.

ALIGNED

True → The data is properly aligned in memory for efficient access.
False → The data is not properly aligned.

WRITEBACKIFCOPY

Usually False.
Used internally by NumPy in certain advanced memory management operations.

"""

"""

The flags attribute helps you understand:

    How the array is stored in memory.
    Whether the array owns its data.
    Whether the array is writable.
    Whether the memory layout is optimized for performance.

"""

# np.info()

    # The np.info() function displays the documentation of a NumPy object, function, class, or module.

"""

Why use np.info()?

Learn how a NumPy function works.
Check the syntax of a function.
Understand function parameters.
View return type and additional details.
Read the built-in documentation without opening a web browser.

"""
import numpy as np 

arr=np.info(np.array)

print(arr)