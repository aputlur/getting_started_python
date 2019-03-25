class MotorBike:

    def __init__(self, name="Default"):
        self.name = name
        print('default constructor ')

    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    # two constructors are not possible in python, there is no overloading.
    # def instance_method(self):
    #     print('instance method')

    def __repr__(self):
        return repr((self.gear, self.speed))


# mb1 = MotorBike([('a',200), ('b',400)])

class MotorBike2:
    def __init__(self, two):
        self.two = two

    def __repr__(self):
        return repr(self.two)


class MotorBike3:

    def __init__(self, name="Default"):
        self.name = name
        # won't print anything
        print('default constructor {}'.format(name))

    def __init__(self, name):
        self.name = name
        print('default constructor {}'.format(name))


a = MotorBike('a', 100)
print(a)

b = MotorBike2(200)
print(b)

default = MotorBike3('anil')
