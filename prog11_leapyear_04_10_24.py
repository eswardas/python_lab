curr_year = 2024
end_year = int(input("Enter the end year:"))

for i in range(curr_year,end_year+1):
    if i%4==0:
        if i%400:
            print(f"{i} is a leap year!")
        elif i%100==0:
            print(f"{i} is a leap year!")
            
