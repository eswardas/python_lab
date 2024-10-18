strr = input("Enter a string:")
print(f"String before swapping:{strr}")
strr2 = strr
temp = strr[0]
strr[0] = strr2[len(strr)-1]
strr2[len(strr)-1] = temp
print(f"String after swapping:{strr2}")
