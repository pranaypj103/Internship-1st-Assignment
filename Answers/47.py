#Write a program to accept a number and find the factorial of the number (using while loop).

fact=1
n=int(input('Enter the number '))
while n!=0:
    fact=fact*n
    n=n-1
print('The factorial of given number is ',fact)