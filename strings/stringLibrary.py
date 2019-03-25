import string

for char in string.ascii_letters:
    print(char)


def print_consonats():
    consonant_string = 'aeiou'
    for char in string.ascii_lowercase:
        if char not in consonant_string:
            print(char)
        else:
            print('not a consonant')

    print('printing consonants')



print_consonats()


def print_string_in_separate_lines(param):
    split = param.split(' ')
    for s in split:
        print(s)



print_string_in_separate_lines('this is a string')