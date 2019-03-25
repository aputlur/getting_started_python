# initialize dict
dict = {1: "one", 2: "two", 3: "three"}
print(dict)

# put new value
dict[4] = 'four'

print(dict)

#get value
print('printing value of 2 : {} '.format(dict[2]))
print('printing value of 3 : {} '.format(dict[3]))

# del val
del dict[4]
print("print all from dict {}: ".format(dict))

# add list to the dictionary
dict[4] = ['four','five','six']
print("print all from dict {}: ".format(dict))

print('print all key-value pairs:')
# iterate over map
for key in dict:
    print('key : {} and value : {} '.format(key,dict[key]))

print(dict.items())
# find if key exists

if 13 in dict:
    print('three exists')
if 4 in dict.keys():
    print('4 exists')
if 'three' in dict.values():
    print('three exists in dict values')

# print squars of first 10 numbers in dict
squares_of_first_10_nums = {i: i*i for i in range(1, 11)}
print(squares_of_first_10_nums)

sum_of_first_10_nums = sum(range(1, 101))
print(sum_of_first_10_nums)

