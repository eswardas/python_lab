def add(a,b):
    print(f"Sum of {a} and {b} :{a+b}")

def sub(a,b):
    print(f"Difference of {a} and {b} :{a-b}")

def multiply(a,b):
    print(f"Product of {a} and {b} :{a*b}")

def divide(a,b):
    if b!=0:
        print( f"Quotient of {a} and {b} :{a/b}")
    else:
        print("Error! Division by zero is not allowed.")