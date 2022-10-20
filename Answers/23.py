#Write a program to accept a number “n” from the user; then display the series 1,3,5,7,9,…,n and find the sum of the numbers in this series.

sum=0
n=int(input('Enter a number:'))
print('The series is :',end=' ')
for i in range(0,n):
    o=2*i+1
    print(o,end=' ')
    sum=sum+o
print('\n',sum)