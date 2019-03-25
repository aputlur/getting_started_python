# strings
print('single quotes is allowed')
print("double quotes also allowed")
print("She said, \"That's great tasting apple!\"")
print('She said, That\'s great tasting apple')

var_1 = 'That\'s great!'
print(var_1)

var_2 = "That's not great!"
print(var_2)

var_3 = "apple"
zeroIndex = var_3[0]
fifthIndex = var_3[4]

print(zeroIndex + " " + fifthIndex)

print('anil'[2].capitalize())

# spliting strings
print('Anil KUmar reddy putluru'.split()[3])

# concatenating string with integer, unlike Java, should convert to str()

print('Length of the string is : ' + str(len('Anil KUmar reddy putluru')))

# Instead concatenating, we can use format
print('{} {} ' .format('Length of the string is =', len('Anil KUmar reddy putluru')))

# Format Specification
print(20 * '-')
print('{0:8} | {1:9} | {2:1} | {3:10}'.format('Name', 'Length', 'yeS/NO','3RD'))
print(20 * '-')
print('{0:8} | {1:9}'.format('Anil', len('Anil')))
print('{0:8} | {1:9} '.format('Kumardddddddddddddddddddddddd',len('Kumar')))
print('{0:8} | {1:9} '.format('Reddy', len('Reddy')))
print('{0:8} | {1:9}' .format('Putluru',len('Putluru')))
print(20 * '-')




# repeating string
print(('Anil KUmar reddy putluru\n') * 2)

#Formatting string

# Practice - 1[ Write program to create three variable and print them]

animal = 'cat'
vegetable = 'broccoli'
mineral = 'gold'
print("here is an animal, and vegetable, and mineral, ")
print(animal)
print(vegetable)
print(mineral)


#Pratice 2 - speech buuble

var1 = 'hello'
print('     {}'.format('_' * len(var1)))
print('     {}'.format(var1))
print('     {}'.format('*' * len(var1)))


# Practice 3, accept input

# String slices
print('Anil kumar reddy putluru '[11:17])
# input_string = input('enter your name')
print('Your name is ')
# print(input_string)

# is title
print('Anil'.istitle())
print('123'.isdigit())
