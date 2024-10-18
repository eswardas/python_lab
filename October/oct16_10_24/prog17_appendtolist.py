lst = []
length = int(input("ENter size of the list:"))
print(f"Enter {length} numbers:")
for i in range(length):
    temp = int(input())
    lst.append(temp)
print(f"Newly created list:{lst}")
