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

