#Write a program to accept 3 numbers from the user and find the biggest of them.

num1 = int(input('Enter the 1st number num1:\n'))
num2 = int(input('Enter the 2nd number num2:\n'))
num3 = int(input('Enter the 3rd number num3:\n'))

if (num1>num2) and (num1>num3):
    largest = num1
elif (num2>num3) and (num2>num1):
    largest = num2
else:
    largest = num3

print('The biggest of the 3 numbers entered is:',largest)