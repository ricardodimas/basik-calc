##################################
# Basik-Calc
# Calculator for basic operations
# Author: Ricardo Dimas
##################################

def sum(a, b):
    print(int(a) + int(b))

def sub(a, b):
    print(int(a) - int(b))

def mult(a, b):
    print(int(a) * int(b))

def div(a, b):
    print(int(a) / int(b))

#def basic_text():
#    a = input('Type in the first number: ')
#    b = input('Type in the second number: ')

def main():
    print('Welcome to Basik-Calc\n')
    operation = input("""Which operation would you like to perform?
    (1) Addition;
    (2) Subtraction;
    (3) Multiplication;
    (4) Division;\n""")

    if int(operation) == 1:
        a = input('Type in the first number: ')
        b = input('Type in the second number: ')
        sum(a, b)

    if int(operation) == 2:
        a = input('Type in the first number: ')
        b = input('Type in the second number: ')
        sub(a, b)

    if int(operation) == 3:
        a = input('Type in the first number: ')
        b = input('Type in the second number: ')
        mult(a, b)

    if int(operation) == 4:
        a = input('Type in the first number: ')
        b = input('Type in the second number: ')
        div(a, b)

if __name__ == '__main__':
    main()

