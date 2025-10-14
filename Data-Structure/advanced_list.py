'''
Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
'''

get_number = int(input('Digite um número: '))
get_list = []

for number in range(2, get_number + 1):
  verification = True
  for prime in range (2, int(number ** 0.5) + 1):
    if number % prime == 0:
      verification = False
      break
  if verification:
    get_list.append(number)

print(f'Lista de números primos entre 1 e {get_number}:\n{get_list}')