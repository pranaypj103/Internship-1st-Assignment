#Write a program to accept the following details of an employee: empno, name and monthly salary; calculate the yearly salary and display the result.

empno = int(input('Enter the Employee number:\n'))
name = input('Enter the Employee name:\n')
monsal = int(input('Enter the monthly salaray:\n'))

anninc = int(monsal)*12

print('Hi {0}! Your employee id is {1}, monthly salary is Rs {2} and yearly salary is Rs {3}.'.format(name,empno,monsal,anninc))