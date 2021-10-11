class Employee:
    count = 0

    def __init__(self, name, desig, salary):
        self.name = name
        self.desig = desig
        self.salary = salary
        Employee.count += 1

    def displayCount(self):
        print("There are %d employees" % Employee.count)

    def displayDetails(self):
        print("Name:", self.name, ", Designation:", self.desig, ", Salary:", self.salary)


if __name__ == "__main__":

    e1 = Employee("John", "Manager", 80000)
    e2 = Employee("Mike", "Team Leader", 50000)
    e3 = Employee("Ramesh", "Programmer", 30000)
    e4 = Employee("Raj", "Assistant", 25000)
    e4.displayCount()
    print("Details of all employee:")
    e1.displayDetails()
    e2.displayDetails()
    e3.displayDetails()
    e4.displayDetails()
