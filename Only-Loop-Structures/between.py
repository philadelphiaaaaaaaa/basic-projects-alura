'''
Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
'''

get_first_number = int(input('Digite um número para o início: '))
get_second_number = int(input('Digite outro número, agora para o final: '))
print('')
number = 1

if get_first_number > get_second_number:
  print('Deu a louquinha em você, né? O primeiro número maior que o segundo.. Mas eu vou inverter e calcular.')
  print('')
  for number in range(get_second_number + 1, get_first_number):
    print(number)
else:
  for number in range(get_first_number + 1, get_second_number):
    print(number)