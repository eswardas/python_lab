import datetime

curr_year = datetime.date.today().year
end_year = int(input("Enter the end year:"))

for i in range(curr_year,end_year+1):
    if (i%4==0 and i%100!=0) or (i%400 == 0 and i%100==0):
        print(f"{i} is a leap year!")

