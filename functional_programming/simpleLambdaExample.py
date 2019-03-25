def single_arg_fun_goes_here(func, data):
    return func(data)


print('cube result : {} '.format(single_arg_fun_goes_here(lambda data: data ** 3, 123)))
print('range result : {}'.format(single_arg_fun_goes_here(lambda data: range(data), 100)))
print('sum result : {}'.format(single_arg_fun_goes_here(lambda data: data + data, 100)))

