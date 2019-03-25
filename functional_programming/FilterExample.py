class FilterExample:

    def filter_odd_numbers(self):
        numbers = range(1, 11)
        print(list(filter(lambda odd_list: odd_list % 2 != 0, numbers)))

    def filter_max_number(self, data):
        print(list(filter(lambda max: max > 90, data)))

    def display_ends_with_at(self, data):
        print(list(filter(lambda strs: strs.endswith('at'), data)))

    def display_len_of_three(self, data):
        print(list(filter(lambda x: len(x) == 3, data)))

    def display_starts_with_a(self, data):
        print(list(filter(lambda x: x.startswith('A'), data)))


FilterExample().filter_odd_numbers()
FilterExample().filter_max_number(range(1, 100))
FilterExample().display_ends_with_at(['Apple', 'Ant', 'Bat'])
FilterExample().display_len_of_three(['Apple', 'Ant', 'Bat'])
FilterExample().display_starts_with_a(['Apple', 'Ant', 'Bat'])
