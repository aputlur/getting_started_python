# def function_name()
# Code block

def hello_function():
    print("welcome to python!")


# declare something with default value
def hello_function(name='there'):
    print('hello {}'.format(name))

def two_arg_function(first,second):
    print('hello {} {}'.format(first,second))

hello_function()
hello_function('anil')
two_arg_function('anil','putluru')

# no return type required what ??

def odd_or_even(number):
    if(number % 2 == 0):
        return 'even'
    else:
        return 'odd'

print('odd or even number ? {} '.format(odd_or_even(5)))
print('odd or even number ? {} '.format(odd_or_even(10)))
