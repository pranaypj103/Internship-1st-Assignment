#Write a program to find the biggest, smallest and sum of the elements in the given 3 X 3 matrix.

import numpy as np

arr = np.array([[5,6,7], [4, 5, 6],[5,6,7]])

print(arr)

l=s=arr[0][0]
sum=0

for i in arr:
    for j in i:
        sum=sum+j
        if j>l:
            l=j
        if j<s:
            s=j
print('The biggest number in the 3 X 3 matrix is:',l)
print('The smallest number in the 3 X 3 matrix is:',s)
print('sum of the elements in the given 3 X 3 matrix is:',sum)