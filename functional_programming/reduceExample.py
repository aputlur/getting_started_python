class ReduceExample:

    def sumExample(self, data):
        print(reduce(lambda x, y: x+y, data))

    def multi(self, data):
        print(reduce(lambda x,y: x*y, data))

    def maxFun(self, data):
        print(reduce(lambda x,y: max(x,y), data))

    def minFun(self, data):
        print(reduce(lambda x,y: min(x, y), data))

    def print_four_letter_words(self):
        words = ['anil', 'kumar', 'reddy']
        print(reduce(lambda x,y: x if len(x) > len(y) else y, words))

ReduceExample().sumExample(range(11))
ReduceExample().multi(range(2, 11))
ReduceExample().maxFun(range(11))
ReduceExample().minFun(range(6, 11))
ReduceExample().print_four_letter_words()

