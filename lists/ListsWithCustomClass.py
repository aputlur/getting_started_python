from operator import attrgetter


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population, self.area))


countries = [Country('India', 1000, 100000),
             Country('China', 2000, 200000),
             Country('Russia', 3000, 300000)]




class ListExamples:
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    values = [3, 3, 5, 4, 4, 3, 5, 5]

    def print_four_letter_words(self):
        new_list = []
        for item in ListExamples.numbers:
            if len(item) == 4:
                new_list.append(item)
        print('size of four list : {}'.format(new_list))


    def list_comprehension_way(self):
        print([item for item in ListExamples.numbers])
        print([item for item in ListExamples.numbers if len(item) == 4])
        print([len(item) for item in ListExamples.numbers])
        print([item for item in ListExamples.values if item %2 != 0])


print(countries)
print(countries[0])

print(countries[0:3])

print(countries.reverse())

countries.append(Country('USA', 400, 400000))

countries.sort(key=attrgetter('name'))

print(countries)
print(max(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('area')))

printFourLetters = ListExamples()
printFourLetters.print_four_letter_words()
printFourLetters.list_comprehension_way()
