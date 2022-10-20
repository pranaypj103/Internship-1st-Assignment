#Write a program to accept a number from the user and find the reverse of the entered number.

n=int(input('Enter any number:'))
print('Reverse of the entered number is ')
while n!=0:
    i=n%10
    print(i,end='')
    n=int(n/10)