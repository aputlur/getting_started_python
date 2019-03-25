# Instances variables not required, you can add dynamically. If you want to enforce it, create argument constructor.


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

