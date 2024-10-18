string = input("Enter the string:")
words = string.split()
val = 0
for i in words:
    for j in words:
        if j==i:
            val+=1
    print(f"'{i}' repeats {val} times")
    val = 0
