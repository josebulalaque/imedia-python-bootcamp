class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sleep(self):
        print("I will sleep for eight hours")

    def introduce(self):
        print(f"I'm {self.first_name} {self.last_name}!")


person1 = Person("Juan", 'Dela Cruz')
person1.introduce()
person1.sleep()

person2 = Person("Maria", 'Lopez')
person2.introduce()
person2.sleep()
