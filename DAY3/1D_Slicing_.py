# Slicing

        # Slicing means select a element in array and return them
    
        # Slicing always returns a new view (not a copied array by default)
        
        # array[10,20,30,40,50]
        # if we want 20,30,40 then use slicing

        # Syntax Slicing:- 

            # array[start : stop : step]

            # but stop is not inculde in output
            # Start is Included 
            # Stop is not Included 

        # [10,20,30,40,50]
        # 1:4
        # output 

            # 20,30,40

# Example:

import numpy as np

arr=np.array([10,20,30,40,50])
print(arr)

print(arr[1:4])
print(arr[2:])
print(arr[:5])

print(arr[0:4])

# Step 

print(arr[0:4:2])

print(arr[0::2])


# Negative Index

print(arr[-1:])

print(arr[-2:])

print(arr[-3:])

# Reverse Slicing

print(arr[::-1])

