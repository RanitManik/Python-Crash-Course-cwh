# This is program 33
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        print(self.salary)


rohan = Employee("Rohan", "1,3,000000")
print("Name: ", rohan.name)
print("Salary:", rohan.salary)

print("---------------------")

rahul = Employee("Rahul", "13,000")
print("Name: ", rahul.name)
print("Salary:", rahul.salary)

print("---------------------")

rohan.get_salary()
rahul.get_salary()
