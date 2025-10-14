dados = {
  'Nome': 'Ádoni Sena',
  'Idade': 19,
  'Altura': 1.80,
  'Ano de Nascimento': 2006
}

for chaves in dados.keys():
  print(chaves)

for valores in dados.values():
  print(valores)

for chaves, valores in dados.items():
  print(chaves, valores)