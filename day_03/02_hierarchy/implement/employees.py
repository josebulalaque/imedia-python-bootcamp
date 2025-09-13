class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)

class Recruiter(Employee):
    def recruit(self):
        return f"{self.name} is recruiting Employees"

class Developer(Employee):
    def create_app(self):
        return f"{self.name} is creating an app"

class Manager(Employee):
    def create_review(self):
        return f"{self.name} is doing an Annual review"

class EngineerMgr(Developer, Manager):
    def introduce(self):
        pass

emp1 = Recruiter("Joseph",123)
emp2 = Developer("Jojo",456)
emp3 = Manager("John",789)
emp4 = EngineerMgr("Mark",999)

print(f"{emp1.name} the Recruiter")
print(emp1.recruit())

print(f"{emp2.name} the Developer")
print(emp2.create_app())

print(f"{emp3.name} the Manager")
print(emp3.create_review())

print(emp4.create_app())
print(emp4.create_review())

