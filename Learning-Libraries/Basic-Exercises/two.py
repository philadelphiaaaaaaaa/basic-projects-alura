'''
Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

"Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"
'''
from random import randrange as rr

your_name = input('Qual é o seu nome? Digite: ')

data = {'Nome': your_name}

while True:
  collect_tokens = rr(1000, 9999)
  if collect_tokens % 2 == 0:
    data['Token'] = collect_tokens
    break
  else:
    continue

print(f'Olá, {data["Nome"]} o seu token de acesso é {data["Token"]}! Seja bem-vindo(a)!')