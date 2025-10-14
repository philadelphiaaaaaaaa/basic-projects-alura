'''
Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.
'''

get_number = int(input('Digite um número para contar a tabuada (1 a 10): '))
counter = 1

if not (1 <= get_number <= 10):
  while not (1 <= get_number <= 10):
    get_number = int(input('Digite um número para contar a tabuada (1 a 10): '))

if 1 <= get_number <= 10:
  for counter in range(0, 10):
    counter += 1
    calculating = get_number * counter
    print(f'{get_number} x {counter} = {calculating}')

