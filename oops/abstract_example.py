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


ref = AB1()
ref.get_ready()
ref.do_the_dish()
ref.cleanup()
