#Write a program to accept a number and print the Fibonacci series up to the entered number.

n_terms = int(input ("Enter the upper bound number to generate the Fibonacci numbers:\n"))
n_1 = 0
n_2 = 1
count = 0

if n_terms <= 0:
    print ("Please enter a positive integer, the given number is not valid")
elif n_terms == 1:
    print ("Fibonacci series up to the entered number is",n_terms,": ")
    print(n_1)
else:
    print ("Fibonacci series up to the entered number is:")
    while count < n_terms:
        print(n_1)
        nth = n_1 + n_2
        n_1 = n_2
        n_2 = nth
        count += 1