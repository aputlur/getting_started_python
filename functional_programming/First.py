# function to calculate sum
def calculate_sum(data):
    return sum(range(data))


def call_any_function_here(func, data):
    return func(data)


# pass function to method
result = call_any_function_here(calculate_sum, 101)
print(result)

# declare it as a variable
func1 = calculate_sum
print(call_any_function_here(func1, 101))

