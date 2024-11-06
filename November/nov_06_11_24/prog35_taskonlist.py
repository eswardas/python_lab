
def greatandlow(lst):
    print(f"Greatest value:{max(lst)} , lowest value : {min(lst)} ")
def sortt(lst):
    l = sorted(lst)
    print(f"Sorted list:{l}")
def evenlist(lst):
    for i in lst:
        if i%2==0:
            even_list.append(i)
    print(f"Even numbers in the list:{even_list}")


size = int(input("Enter the size of the list:"))
lst = []
even_list = []
print(f"Enter {size} numbers to the list:")
for i in range(size):
    num = int(input())
    lst.append(num)

while True:
    state = int(input("1.Greatest and lowest in the list\n2.Sorted list in ascending order\n3.List of even numbers\n4.Exit\n"))
    if state==1:
        greatandlow(lst)
    elif state==2:
        sortt(lst)
    elif state==3:
        evenlist(lst)
    elif state==4:
        break
print("................................................\n")
            

    
