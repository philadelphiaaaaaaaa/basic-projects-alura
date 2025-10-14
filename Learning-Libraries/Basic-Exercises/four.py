'''
Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro.
'''
from math import sqrt as raiz

numeros = [2, 8, 15, 23, 91, 112, 256]

for i in numeros:
  calculating = raiz(i)
  if (calculating // 1 == calculating) == True:
    print(f'{calculating} é inteiro.')
  else:
    print(f'{calculating} não é inteiro.')