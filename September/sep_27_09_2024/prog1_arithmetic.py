num1 = int(input("Enter 1st number:\n"))
num2 = int(input("ENter 2nd number:\n"))

choice = int(input("Enter the operation number:\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n"))
if choice == 1:
    print(f"{num1}+{num2}={num1+num2}")
elif choice == 2:
    print(f"{num1}-{num2}={num1-num2}")
elif choice == 3:
    print(f"{num1}/{num2}={num1/num2}")
elif choice == 4:
    print(f"{num1}*{num2}={num1*num2}")
    
