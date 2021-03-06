# declare list
items = ['mobile', 'laptop', 'car']

# print all items
print(items[0])
print(items[1])
print(items[1])

# print items in reverse order
print(items[-2])
print(items[-1])
print(items[-0])

# append one item
items.append('weekEnd')

# add more items
more_items = ['sat', 'sun']
items.extend(more_items)
print(items)

# add more items
items.extend(['mon', 'tue', 'thanks'])
print(items)

# insert first
items.insert(0, 'anil')

# insert third
items.insert(3, 'putluru')

# slices

print(items[1:4])
print(items[:5])
print(items[5:])
print(items[-3:])
print(items[0:len(items)])

# exception handling

try:
    there = items.index['cruise']
except:
    there = 'not there'
print(there)

# Sorting
sorted_list = sorted(items)
print('non sorted list : {}'.format(items))
print('sorted list : {}'.format(sorted_list))


def second_method_with_params(count):
    print("hello world")
    for i in range(1, count + 1):
        print("hello-world -> ", i)


def squares_of_numbers(number):
    for i in range(1, number + 1):
        print(i * i)


def sort():
    for item in sorted(items, key=len, reverse=False):
        print(item)


second_method_with_params(5)
squares_of_numbers(6)
sort()
