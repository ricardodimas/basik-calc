##################################
# Basik-Calc
# Calculator for basic operations
# Author: Ricardo Dimas
##################################

def sum(a, b):
    print(int(a) + int(b))

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
        

if __name__ == '__main__':
    main()

