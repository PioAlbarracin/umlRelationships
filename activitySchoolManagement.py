class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_info(self):
        return f"Name: {self.name}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = value

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self):
        return f"{self.name} is studying."

person1 = Person("Lina", 20)
student1 = Student("Lina", 20)

print(person1.get_info()) # For the person class
print(f'Age: {person1.age}\n') 

#It is better because it encapsulates the attribute age, and is only accessed via the getter method. Which is detected by the computer and is then printed without issue.

print(student1.get_info()) # For the student class
print(student1.study())

