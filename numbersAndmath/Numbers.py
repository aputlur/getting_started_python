print('Sum {}'.format(1 + 2))
print('Substract {} '.format(1 - 2))
print('Divide {}'.format(68 / 2))
print('Product {}'.format(1 * 2))
print('power {} '.format(2 ** 31))
print('modulo {} '.format( 56 % 2))

# When you try to append Integer string to int, it will throw an error, hence convert into int() before doing so
# Error : TypeError: can only concatenate str (not "int") to str

integer_string = '3'
print(int(integer_string) + 2)

# convert to float
print(float(integer_string) + 2)

"""comments can be written like this, it's a valid comment"""
