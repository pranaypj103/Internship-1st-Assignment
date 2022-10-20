#Write a program to accept a number from the user and count the number of digits in the number.

count=0
n=int(input('Enter any number:'))
while n!=0:
    count=count+1
    n=int(n/10)
print('The number of digits in the entered number is',count)