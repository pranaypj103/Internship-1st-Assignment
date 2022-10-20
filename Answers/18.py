#Write a program to accept the lower bound number and the upper bound number from the user and print the prime numbers between them.

a = int(input('Enter the lower bound value: '))
b = int(input('Enter the upper bound value: '))
print('The prime numbers between',a,'and',b,'are:\n',end=' ')
for num in range(a,b+1):
   if num > 1:
       for i in range(2,num):
           if (num%i)==0:
               break
       else:
           print(num)