from random import choice
from random import randrange
from math import pow

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
print(choice(lista))
print(randrange(100))


first_number = float(input('Digite um número: '))
second_number = float(input('Digite outro número: '))
calculating = pow(first_number, second_number)
print(calculating)