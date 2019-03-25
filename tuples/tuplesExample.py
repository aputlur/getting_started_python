tuple_var = ('a', 'b', 'c')
print("printing tuple var : {} ".format(tuple_var))
print("get zero index : {} ".format(tuple_var[0]))
print("get zero index : {} ".format(tuple_var[1:3]))
# tuples are immutable and cannot initialized with new values.
# tuple_var[4] = 'd'

print("printing tuple var : {} ".format(tuple_var))

# it supports all the options like a list


list_from_tuple = list(tuple_var)

print('tuple to a list : {} '.format(list_from_tuple))

tuple_from_list = tuple(list_from_tuple)

print('tuple from a list : {}'.format(tuple_from_list))

print('max element : {}'.format(max(tuple_from_list)))
print('min element : {}'.format(min(tuple_from_list)))

tuple1 = ('anil', 33, 1985,'USA')
print(tuple1)
name,age,year, country = tuple1

print(tuple1[3])

