def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    print(f"\n{num} factorial = {fact}")