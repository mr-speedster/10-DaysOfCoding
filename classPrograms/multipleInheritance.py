class Employee:
    name=""
    age=0
    phone=0
    address=""
    salary=0
    def printSalary(self):
        print("Salary:"+self.salary)
    def __init__(self,name,age,phone,address,salary):
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address
        self.salary=salary
    def employeeDisplay(self):
        print("Name"+self.name)
        print("Age"+self.age)
        print("Phone"+self.phone)
        print("Address"+self.address)
        print("Salary"+self.salary)
class Manager(Employee):
    specialization=""
    department=""
    def __init__(self, name, age, phone, address, salary,specialization,department):
        super().__init__(name, age, phone, address, salary)
        self.specialization=specialization
        self.department=department
    def managerDisplay(self):
        Employee.employeeDisplay()
        print("Specialization"+self.specialization)
        print("Department"+self.department)
class Officer(Employee):
    specialization=""
    department=""
    def __init__(self, name, age, phone, address, salary,specialization,department):
        super().__init__(name,age,phone,address,salary)
        self.specialization=specialization
        self.department=department
    def OfficerDisplay(self):
        Employee.employeeDisplay()
        print("Specialization"+self.specialization)
        print("Department"+self.department)
class Test(Manager,Officer):
    print("Enter the manager deatils")
    name=input("Enter the name")
    age=int(input("Enter the age"))
    phone=int(input("Enter the Phone Number"))
    address=input("Enter the address")
    salary=int(input("Enter the Salary"))
    special=input("Enter the specialization")
    dept=input("Enter the department")
    manager=Manager(name,age,phone,address,salary,special,dept)
    manager.managerDisplay()

    print("Enter the Officer deatils")
    name1=input("Enter the name")
    age1=int(input("Enter the age"))
    phone1=int(input("Enter the Phone Number"))
    address1=input("Enter the address")
    salary1=int(input("Enter the Salary"))
    special1=input("Enter the specialization")
    dept1=input("Enter the department")
    officer=Officer(name1,age1,phone1,address1,salary1,special1,dept1)
    officer.OfficerDisplay()
