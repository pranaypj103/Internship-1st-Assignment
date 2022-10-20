#The Sports Club registration form has the following details: name, mobile number and age. Per the membership policy, the person should be at least 18 years old to become a member. Write a program to accept the details mentioned above; if the age is >18 years then display the entered details with a congratulatory message, else the following message should be displayed “Sorry! You need to be at least 18 years old to get membership.”

from unicodedata import name

name = input('Enter the name:\n')
phno = int(input('Enter the phone number:\n'))
age = int(input('Enter the age:\n'))

if age<18:
    print('Sorry! You need to be at least 18 years old to get membership.')
else:
    print('Congratulations {0} for your successful registration.'.format(name))