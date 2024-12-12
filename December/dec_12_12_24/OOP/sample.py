from classes.employee import Employees

name = input("Enter employee name:\n")
id = int(input("Enter the ID:"))
salary  = int(input("Enter the salary:"))

details = Employees(name,id,salary)
details.employee_details()
