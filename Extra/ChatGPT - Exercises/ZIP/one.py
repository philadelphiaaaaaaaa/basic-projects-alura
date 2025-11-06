frutas = ['maçã', 'banana', 'uva']
cores = ['vermelha', 'amarela', 'roxa']

print(list(zip(frutas, cores)))

for nome, cor in zip(frutas, cores):
  print(f'A fruta {nome} é {cor}')