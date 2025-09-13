class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with id {self.id}")

    def add_task(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)

employee1 = Employee("Richard",123)
employee2 = Employee("Jelly",456)

#print(employee1.name)

employee1.add_task("Create Slides")
employee2.add_task("Present Report")






