#Write a program to accept the billing amount, if it is > 6000 then give a discount of 10% and display the net amount.

bill = float(input('Enter the billing amount:\n'))

if bill>6000:
    discount = bill*float(0.9)
    print('Your net billing amount: {0}'.format(discount))

else:
    print('Your net billing amount: {0}'.format(bill))