#Write a program to accept the principal amount, rate of interest, time and calculate the simple interest.

p = float(input('Enter the principal amount:\n'))
r = float(input('Enter the rate of interest:\n'))
t = float(input('Enter the time (years):\n'))

si = (p*t*r)/100

print('Simple Interest is: {0}'.format(si))