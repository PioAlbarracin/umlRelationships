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

person1 = Person("Lina", 20)

print(person1.get_info())
print(f'Age: {person1.age}') 

#It is better because it encapsulates the attribute age, and is only accessed via the getter method. Which is detected by the computer and is then printed without issue.