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
#iterate over map
for key in dict:
    print('key : {} and value : {} '.format(key,dict[key]))

#find if key exists

if 13 in dict:
    print('three exists')
if 4 in dict.keys():
    print('4 exists')
if 'three' in dict.values():
    print('three exists in dict values')