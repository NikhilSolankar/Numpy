# Copy & View

        # Sometimes we want to create another array.

        # There are 2 ways to do that.

                # Copy
                # View

        # The biggest question is:

        # If we change the new array, should the original array also change?

        # Depending on the answer, we use Copy or View.

# copy()

        # copy() creates a completely new array.
        # It allocates new memory.
        # Original array and copy array has two different memory locations
        # The original array and copied array are completely independent.

        # Syntax

            # arr2=arr.copy()

# Example: 

import numpy as np

arr=np.array([10,20,30,40,50])
arr2=arr.copy()
print(arr)
print(arr2)

arr2[0]=100
print()
print(arr)
print(arr2)

# Notice Original array is not change 
# [10 20 30 40 50]

# only copy changed
# [100  20  30  40  50]

# -----------------------------------------------------------------

# view()

        # view() does NOT create new data / array
        # if we create a view of array then 
        # both are point to same memory

        # if we chnage the view array then if effect on original and view array
        # because both point same memory location

# Example:

arr=np.array([100,200,300,400,500])

arr2=arr.view()
print()
print(arr)
print(arr2)

# Modify 

arr[0]=111

print(arr)
print(arr2)

print(arr.base)

# If Output is None Then
# It owns its memory.

print(arr2.base)

# If Output is Not None Then
# It is sharing memory.

# Notice modification is effect on both array

