#Write a program to accept a number from the user and print its multiplication table (upto “times 10”).

num = int(input('Enter the number to generate its multiplication table: '))

print('Multiplication table for',num,'is:\n')
for i in range(1,11):
    mul = num*i
    print('{0}*{1}={2}'.format(num,i,mul))