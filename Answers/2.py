#Write a program to accept the weight of 3 persons, calculate the total weight, determine the average weight and display these details.

from audioop import avg

p1 = float(input('Enter the weight of the first person: '))
p2 = float(input('Enter the weight of the second person: '))
p3 = float(input('Enter the weight of the third person: '))

sum = p1+p2+p3
avg = float(sum)/3

print('The sum of weight of the 3 persons is {0} Kgs and the average weight is {1} Kgs'.format(sum,avg))