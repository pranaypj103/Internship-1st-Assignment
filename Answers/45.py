#Write a program to accept a number from the user and calculate the sum of digits of the number; repeat the operation till the sum gets to be a single digit number.

sum=0
count=0
n=int(input('Enter any number:'))
while n!=0:
    i=n%10
    sum=sum+i
    count=count+1
    n=int(n/10)
    if n==0 and count>1:
        n=sum
        sum=0
        count=0
print('Single digit sum is:',sum)