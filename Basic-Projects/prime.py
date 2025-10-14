'''
Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''

get_number = int(input('Digite um número para verificação se é primo ou não: '))

if get_number < 2:
  print('Loop encerrado, este número não é primo!')
else:
  verification = True
  for i in range (2, int(get_number ** 0.5) + 1):
    if get_number % i == 0:
      verification = False
      break
  if verification:
    print('Verificado! Este número é primo!')
  else:
    print('Loop encerrado, este número não é primo!')