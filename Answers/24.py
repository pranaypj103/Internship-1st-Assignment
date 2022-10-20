#Write a program to accept a number “n” from the user; find the sum of the series 1/23+1/33+1/43……..+1/n3.

sum=0
n=int(input('Enter a number:'))

for i in range(2,n+1):
    sum=(1/i**3)+sum
print(sum)