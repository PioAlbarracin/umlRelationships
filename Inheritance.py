class Zoo:
    def __init__(self, name: str):
        self.name = name

class Tiger(Zoo):
    def roar(self):
        return print(f'{self.name} says roar')

MaleTiger = Tiger(name="Male Tiger")

MaleTiger.roar()
