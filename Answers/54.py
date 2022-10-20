#Write a program to add the first 7 terms of the following series using a for loop:
#1/1!+2/2!+3 /3!+....

sum=0
f=1
for i in range(1,8):
    n=i
    while n!=0:
        f=f*n
        n=n-1
    res=i/f
    if n==0:
        f=1
    sum=sum+res
print(sum)