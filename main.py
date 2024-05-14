
class Breeding:

    def __init__(self, breed_number: int):
        self.adults = 0
        self.teens = 1
        self.babies = 0
        self.breed_number = breed_number

    def age(self):
        print("age")
        self.adults += self.teens
        self.teens = self.babies


    def breed(self):
        self.babies = self.adults * self.breed_number
        print(self.adults)
        print(self.teens)
        print(self.babies)


def cycle(breeding : Breeding, sequence):
    for turn in range(1, sequence):
        breeding.age()
        breeding.breed()

breed = Breeding(3)

cycle(breed, sequence=3)