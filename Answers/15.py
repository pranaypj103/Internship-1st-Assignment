#Write a program to generate the first 'N' natural numbers. Accept the value of 'N' from the user.

num = int(input('Enter the number of natural numbers to be generated:\n'))

print('The first ',num,' numbers are:')
for i in range(1,num+1):
    print(i,end=" ")