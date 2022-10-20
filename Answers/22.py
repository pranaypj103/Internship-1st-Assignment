#Write a program to accept a number “n” from the user; then display the sum of the series 1+1/2+1/3+……….+1/n.

sum=0
n=int(input('Enter a number:'))
for i in range(1,n+1):
    sum=(1/i)+sum
print(sum)