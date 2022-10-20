#Write a program to accept a five digit number from the user, increment each digit by one and display the number (digit 9 gets incremented to 0).

sum=0
i=0
n=int(input('Enter a number '))
while n!=0:
    r=n%10
    if r==9:
        a=0
    else:
        a=r+1
    n=n//10
    sum=sum+a*10**i
    i=i+1
print(sum)