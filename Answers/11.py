#Write a program to accept two numbers num1 and num2; when one is subtracted from the other, the result should always be a positive number.

num1 = int(input('Enter the first number num1:\n'))
num2 = int(input('Enter the second number num2:\n'))

diff = num1-num2

if diff>0:
    print('The result (difference) is: {0}'.format(diff))
else:
    temp = diff*(-1)
    print('The result (difference) is: {0}'.format(temp))