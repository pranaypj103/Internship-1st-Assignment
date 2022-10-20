#Write a program to accept a number from the user and determine whether it is an Armstrong number or not.

num = int(input('Enter the three digit number to be checked for Armstrong: '))
t = num
cube_sum = 0

while t!= 0:
    k = t % 10
    cube_sum += k**3
    t = t//10
if cube_sum == num:
    print(num, ' is an Armstrong Number')
else:
    print(num, 'is not a Armstrong Number')