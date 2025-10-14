'''
Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.
'''

from datetime import date

get_day = int(input('Digite o dia (1 a 30): '))
while get_day > 30 or get_day < 1:
  get_day = int(input('Dia inválido, informe-o novamente, por favor (1 a 30): '))


get_month = int(input('Digite o mês (1 a 12): '))
while get_month > 12 or get_month < 1:
  get_month = int(input('Mês inválido, informe-o novamente, por favor (1 a 12): '))

get_year = input('Digite o ano: ')
while len(get_year) != 4 or not get_year.isdigit() or get_year > str(date.today().year):
  get_year = input('Ano inválido, informe-o novamente, por favor: ')

get_year = int(get_year)

print(f'\nAnálise completa, validado com sucesso:\n-> Ano: {get_year}\n-> Mês: {get_month}\n-> Dia: {get_day}')