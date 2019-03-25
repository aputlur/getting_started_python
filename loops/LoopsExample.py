items = ['anil', 'mobile', 'laptop', 'putluru', 'car', 'weekEnd', 'sat', 'sun', 'mon', 'tue', 'thanks']


# for item in items:
#     print(item.upper())
#
# counter = 0
# while (counter < len(items)):
#     print(items[counter])
#     counter += 1
#
# for i in range(0, 19):
#     print(i)


# is prime or not

def is_prime(number):
    if number < 2:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False

    return True


def sum_upto_n(number):
    sumUptoN = 0
    for num in range(number + 1):
        sumUptoN += num
    return sumUptoN


def printTriangle(number):
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


# while loop
def print_squares_of_number_below(limit):
    i = 1
    while i * i < limit:
        print(i * i, end=" ")
        i += 1


# do-while replacement in python
def ask_question():
    number = 0  # initialize condition with true
    while number >= 0:
        number = int(input('Enter a number'))
        print(f" cube is {number ** 3}")


print('Is 5 is prime : {} '.format(is_prime(6)))
print(sum_upto_n(100))
printTriangle(10)
print_squares_of_number_below(100)
ask_question()
