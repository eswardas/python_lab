class Employees:

    company_name = "No scam pvt ltd"
    place = "Kunnamkulam"

    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary

    def employee_details(self):
        print( f"Name:{self.name}, ID:{self.id}, Salary:{self.salary}")

    
