try:
    1 / 0
except ZeroDivisionError as error:
# except (ZeroDivisionError, ValueError):
    print('any number cannot be divided by zero')
    print(error)
finally:
    print('this executed')


class Amount:
    def __init__(self, currency, amout):
        self.currency = currency
        self.amount = amout

    def add(self, other):
        if self.currency == other.currency:
            self.amount = other.amount
        else:
            # raise Exception('currency is not same')
            raise CustomException(self.currency + " do not match with " + other.currency)


class CustomException(Exception):
    def __init__(self, errorMsg):
        # super().__init__(errorMsg)
        # super(errorMsg)
        print('nothing')

amt1 = Amount('USD', 12)
amt2 = Amount('USD',12)
amt3 = Amount('INR',12)

try:
 amt2.add(amt1)
 amt2.add(amt3)
except CustomException as errorMsg:
    print (errorMsg)