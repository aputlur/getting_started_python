from enum import Enum


class Currency(Enum):
    USD = 1
    EUR = 2
    INR = 3

print(Currency.USD)

for currency in enumerate(Currency):
    print(currency.INR)
