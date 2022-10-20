#Write a program to generate the first 'N' natural numbers and print them in descending order.

n = int(input('Enter the number of natural numbers to be generated:'))

print('The first 5 natural numbers in descending order are:\n')
for i in range(n,0,-1):
    print(i,end=" ")