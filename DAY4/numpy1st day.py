# Array Basic

import numpy as np 

tem=np.array([32.4,45.32,45.22,32.23])

avg=np.mean(tem)

print(avg)


import numpy as np

arr=np.array([1,2,3,4,5,6,7])
print(arr)

z=np.zeros(4)
print(z)

o=np.ones(4)
print(o)

o1=np.ones((4,2))
print(o1)

f=np.full(4,5)
print(f)

f=np.full((4,4),7)
print(f)


# creating sequence of numbers in numpy

#arange()

#arange(start,stope,step)

import numpy as np

numbers=np.arange(1,11,1)
print(numbers)

#Step change 2
numbers1=np.arange(1,11,2)
print(numbers1)

# creating identity matrix
#eye(size)

import numpy as np

iden=np.eye(5)
print(iden)
