#Write a program to accept a four digit number from the user and display its denomination.

n=int(input('Enter a four digit number '))
sum=0
i=4
while n!=0 and i!=0:
    a=n//10**(i-1)
    b=a%10
    d=10**(i-1)
    i=i-1
    print(b,' * ',d,' = ',b*d)