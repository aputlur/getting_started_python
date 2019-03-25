class StaticClass:
    # this is static be default
    count = 0

    def __init__(self, name):
        self.name = name
        StaticClass.count += 1

    @staticmethod
    def get_count():
        return StaticClass.count


sc1 = StaticClass('messi')
print(sc1.get_count())
sc2 = StaticClass('anil')
print(sc2.get_count())
sc3 = StaticClass('anil')
print(sc3.get_count())
print(StaticClass.get_count())