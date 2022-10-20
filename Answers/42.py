#Write a program to accept a number from the user and find the sum of digits in the entered number.

sum=0
n=int(input('Enter any number:'))
while n!=0:
    i=n%10
    sum=sum+i
    n=int(n/10)
print('The sum of digits of the entered number is',sum)