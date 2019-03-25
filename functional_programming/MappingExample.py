class MappingExample:

    def map_to_a_list_in_upper_case(self, data):
        print(list(map(lambda x: x.upper(), data)))

    def square(self, data):
        print(list(map(lambda sq: sq * sq, range(data))))


MappingExample().map_to_a_list_in_upper_case(['Anil','Kumar', 'Reddy'])
MappingExample().square(10)