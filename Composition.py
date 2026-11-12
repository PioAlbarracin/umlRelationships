class Zoo:
    def __init__(self, name: str):
        self.name = name

class Cages(Zoo):
    def __init__(self):
        self.zoo_cages = [Zoo("Tiger Cage"), Zoo("Penguin Cage")]

my_zoo_cages = Cages()

for cage in my_zoo_cages.zoo_cages:
    print(f'Cage created: {cage.name}')
