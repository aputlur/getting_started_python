OOPS
------------
multiple inheritance is supported.

no interface support

abstract class also exists.

polymorphism also supported.

multiple constructors is not possible in python. Overloading is not possible

Instances variables not required, you can add dynamically. If you want to enforce it, create argument constructor.

Overriding behavior
----

````
class Planet:
    pass


earth = Planet()
mars = Planet()

# dynamically add attributes to the class
earth.name = 'Earth'
earth.water = '3 over fourth'
print(earth.name)
print(earth.water)

mars.name = 'does not have attribute'
print(mars.name)

````

Multiple Inheritance is possible
----

````
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


````

Abstract class
----

````

from abc import ABC, abstractmethod


class AbstractReceipe(ABC):
    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.cleanup()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def do_the_dish(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class AbstractReceipeImpl(AbstractReceipe):

    def get_ready(self):
        print('get_ready called')

    def do_the_dish(self):
        print('do_the_dish called')

    def cleanup(self):
        print('cleanup called')


ref = AbstractReceipeImpl()
ref.get_ready()
ref.do_the_dish()
ref.cleanup()


````

Polymorphism and Duck Typing
----

````
from abc import ABC, abstractmethod


class AbstractReceipe(ABC):
    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.cleanup()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def do_the_dish(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class AB1(AbstractReceipe):

    def get_ready(self):
        print('get_ready called')

    def do_the_dish(self):
        print('do_the_dish called')

    def cleanup(self):
        print('cleanup called')
    
    def cleanup1(self):
        print('cleanup called')
        

class AB2(AbstractReceipe):

    def get_ready(self):
        print('AB2 get_ready called')

    def do_the_dish(self):
        print('AB2 do_the_dish called')

    def cleanup(self):
        print('AB2 cleanup called')


receipes = [AB1(), AB2()]
for r in receipes:
    r.get_ready()
    r.do_the_dish()
    r.cleanup()
    # end up with since AB2 does not have cleanup1()
    # r.cleanup1()
    


````

