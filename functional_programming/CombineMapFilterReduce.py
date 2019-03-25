numbers = range(1, 11)

result = reduce(lambda x, y: x+y, (map(lambda y: y*y, filter(lambda x: x % 2 != 0, numbers))))
print(result)

# months value sum
months = [('Jan', 31), ('Feb', 28), ('Mar', 31)]
print(sum(map(lambda x: x[1], months)))

# find month which has least days

print(tuple(reduce(lambda x, y: min(x, y), months))[0])

