#Write a program to accept two numbers num1, num2 and an operator. Simulate the calculator using switch statement.

def add():
    print(num1+num2)

def sub():
    print(num1-num2)

def mul():
    print(num1*num2)

def mod():
    print(num1%num2)

def div():
    print(num1/num2)

def switch(o):
    switcher={
        1: add(),
        2: sub(),
        3: mul(),
        4: mod(),
        5: div(),
    }
    return switcher.get(o,'invalid')

num1=int(input('Enter the 1st Operand num1: '))
num2=int(input('Enter the 2nd Operand num2: '))
print('1.add 2.sub 3.mul 4.mod 5.div')
o=int(input('Enter the operator '))
switch(o)