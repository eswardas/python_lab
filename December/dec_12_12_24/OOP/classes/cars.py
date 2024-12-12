class Cars:

    def __init__(self,company,price,color):
        self.company = company
        self.price = price
        self.color = color

    def car_details(company,price,color):
        return f"Company: {company}, Price: {price}, Color: {color}"
    
total = 3
print("Enter the details of 3 cars:\n")
for i in range(1,4):
    print(f"\nEnter Car {i} details:\n")
    company = input("Enter the company name: ")
    price = int(input("Enter the price: "))
    color = input("Enter the color of the car:")
    car = Cars.car_details(company,price,color)
    print(f"Car{i} details:{car}")
  

# car1 = Cars.car_details("Honda",120000,"red")
# print(f"Car 1 details:{car1}\n")

# car2 = Cars.car_details("Lamborgini",67000000,"black")
# print(f"Car 2 details:{car2}\n")

# car3 = Cars.car_details("Tata",900000,"white")
# print(f"Car 3 details:{car3}\n")