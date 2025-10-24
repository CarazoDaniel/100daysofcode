from art import logo

def add(a,b):
    """This function will return the sum"""
    return a + b

def sub(a,b):
    """This function will return the substraction"""
    return a - b

def mult(a,b):
    """This function will return the multiplication"""
    return a * b

def pot(a,b):
    """This function will return a to the pot of b"""
    result = 0
    for i in range(b):
        result = a*a
    return result

def div(a,b):
    """This function will return the division a/b"""
    return a / b


calculator = {'+':add,'-':sub, "*":mult, "^":pot, "/":div}
print(logo)

go = True
num1 = float(input("Type your first number: "))

while go:
    calc = input("Type the operation desired ('+''*''^''/''-') ").lower()
    num2 = float(input("Type your second number: "))
    print(f'the result of {num1} {calc} {num2}')
    num1 = calculator[calc](num1,num2)
    print(f"is {num1}")
    if input("Do you wish to keep doing operations with the result? 'y' 'n'").lower() == 'n':
        print('\n' * 25)
        num1 = float(input("Type your first number: "))

