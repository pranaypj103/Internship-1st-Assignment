#Write a program to accept a number, if it is negative then convert it to a positive number.

num = float(input('Enter a number:\n'))

if num<0:
    temp = num*(-1)
    print('The result is: {0}'.format(temp))

elif num>0:
    print('The result is {0}'.format(num))

else:
    print('The result is Zero.')