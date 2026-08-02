# 2D Slicing

        # 2D slicing is a extension on 1D slicing
        # 2D Slicing means selecting rows and columns from a 2D array.
        
        # Syntax
        # array[row,column]
        # arr[0:3,0:2]

        # Always pass first row and second column  


import numpy as np

arr=np.array(
    [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]    
    )

print(arr[0:2,0:2])
print(arr[0:4,0:1])
print(arr[1:3,1:3])
print(arr[0:4,1:2])
print(arr[:,1:]) # means All rows and column start with 1
print(arr[:,0])
print(arr[1,:])
print(arr[:,:])
print(arr[::2,:])
print(arr[:,::2])
