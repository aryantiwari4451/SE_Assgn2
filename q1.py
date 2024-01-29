class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, id, name, age, salary):
        self.employees.append(Employee(id, name, age, salary))

    def sort_by(self, parameter):
        if parameter == "Age":
            self.employees.sort(key=lambda x: x.age)
        elif parameter == "Name":
            self.employees.sort(key=lambda x: x.name)
        elif parameter == "Salary":
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid parameter")

    def print_table(self):
        for employee in self.employees:
            print(f"Employee ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

# Usage
table = EmployeeTable()
table.add_employee("161E90", "Ramu", 35, 59000)
table.add_employee("171E22", "Tejas", 30, 82100)
table.add_employee("171G55", "Abhi", 25, 100000)
table.add_employee("152K46", "Jaya", 32, 85000)

print("Choose a sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")
choice = input("Enter your choice (1-3): ")

if choice == "1":
    table.sort_by("Age")
elif choice == "2":
    table.sort_by("Name")
elif choice == "3":
    table.sort_by("Salary")
else:
    print("Invalid choice")

table.print_table()
