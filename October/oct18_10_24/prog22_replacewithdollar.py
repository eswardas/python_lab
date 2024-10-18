strr = input("Enter a string:")
first = strr[0]
res = first+strr[1:].replace(first.lower(),'$')
print(res)
