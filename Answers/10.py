#Write a program to accept two numbers from the user and determine bigger of the two.

num1 = float(input('Enter the first number num1:\n'))
num2 = float(input('Enter the second number num2:\n'))

if num1>num2:
    print('The bigger of the two numbers entered ({0} and {1}) is: {0}'.format(num1,num2))
else:
    print('The bigger of the two numbers entered ({0} and {1}) is: {1}'.format(num1,num2))