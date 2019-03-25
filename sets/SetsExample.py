values = [3, 3, 5, 4, 4, 3, 5, 5]
filtered_set = set(values)
print(filtered_set)
print(5 in filtered_set)
print(min(filtered_set))
print(max(filtered_set))
print(sum(filtered_set))

range_set = set(range(1, 3))
# union of sets
print(range_set | filtered_set)

# intersection of sets
print(range_set - filtered_set)
