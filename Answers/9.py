#Write a program to accept a number from the user and determine whether it is even or odd

num = int(input('Enter a number:\n'))

if num%2==0:
    print('The entered number {0} is even'.format(num))

else:
    print('The entered number {0} is odd'.format(num))