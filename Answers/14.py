#Write a program to accept the marks scored in three subjects; determine the sum and average of the entered marks. Grade is awarded based on following criteria.
#If average is < 35 -- “C”; >35 and <60 -- “B”; Otherwise -- “A”

sub1 = float(input('Enter the marks scored in 1st subject:\n'))
sub2 = float(input('Enter the marks scored in 2nd subject:\n'))
sub3 = float(input('Enter the marks scored in 3rd subject:\n'))

total = sub1+sub2+sub3
avg = total/3
if (avg<35):
    grade ='C'
elif (avg<65) and (avg>35):
    grade = 'B'
else:
    grade = 'A'

print('Total marks:',total)
print('Average is:',avg)
print('Grade:',grade)