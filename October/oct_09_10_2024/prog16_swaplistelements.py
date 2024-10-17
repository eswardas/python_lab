lst = []
temp = 0
length = int(input("Enter the size of the list:"))

print(f"Enter {length} numbers:")
for i in range(length):
    temp = int(input())
    lst.append(temp)

print(f"List before swapping:{lst}")

temp = lst[0]
lst[0] = lst[length-1]
lst[length-1] = temp

print(f"List after swapping:{lst}")
