#Write a program to accept a number and determine whether it is a prime number or not.

num = int(input('Enter any number: '))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("The entered number",num,"is not a prime number")
            break
    else:
        print("The entered number",num,"is a prime number")
else:
    print("The entered number",num,"is not a prime number")