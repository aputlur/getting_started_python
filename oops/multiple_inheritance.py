class LandAnimal:
    def walk(self):
        print('can walk')


class WaterAnimal:
    def swim(self):
        print('can swim')


class Amphibian(LandAnimal, WaterAnimal):
    pass


frog = Amphibian()
frog.walk()
frog.swim()
