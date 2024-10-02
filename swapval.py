num1 = int(input("ENter num1:"))

num2 = int(input("Enter num2:"))

print(f"Before swapping\nnum1 = {num1} and num2 = {num2}")

num1 += num2
num2 = num1 - num2
num1 -= num2


print(f"After swapping\nnum1 = {num1} and num2 = {num2}")
