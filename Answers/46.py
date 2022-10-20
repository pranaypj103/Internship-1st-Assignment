#Write a program to accept a number from the user and count the number of prime digits.

n=int(input('Enter any number '))
num=0
while n!=0:
    rem=n%10
    n=n//10
    i=1
    count=0
    while i<rem:
        if rem%i==0:
            count=count+1
        i=i+1
    if count>1:
        num=num
    elif rem==1:
        num=num
    else:
        num=num+1
print('Number of prime digits in the entered number:',num)