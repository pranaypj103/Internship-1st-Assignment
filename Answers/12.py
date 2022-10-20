#In a shopping mall, privileged customers (if they have a membership card) are being given a 10% discount on the billed amount, and the others are being given a 3% discount. Write a program to accept the billing amount and confirm the membership card from the customer; calculate and display the net amount to be paid by the customer.

amount = float(input('Enter the bill amount:\n'))
membersh = input('Do you have membership card?\n')

if membersh=='yes':
    disc = amount*(0.1)
    netpay = amount-disc
    print('Thank you! Your total bill amount is Rs {0}, discount is Rs {1} and net amount payable is Rs {2}.'.format(amount,disc,netpay))
else:
    disc = amount*(0.03)
    netpay = amount-disc
    print('Thank you! Your total bill amount is Rs {0}, discount is Rs {1} and net amount payable is Rs {2}.'.format(amount,disc,netpay))