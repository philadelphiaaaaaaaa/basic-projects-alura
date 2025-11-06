'''
Alunos = [lista com os nomes dos alunos]
Notas = [Lista com as notas dos alunos]

1. Criar um dicionário com zip() relacionando par chave-valor (aluno, nota)
2. Percorrer o dicionário e imprimir apenas os alunos com nota maior que 7.0
'''

alunos = ['Ana', 'Pedro', 'João', 'Clara']
notas = [9.5, 7.0, 6.5, 8.0]
dados_alunos = dict(zip(alunos, notas))

for nm, nt in dados_alunos.items():
  if nt > 7.0:
    print(f'[ALTA NOTA] O(a) aluno(a) {nm} está acima da média com uma nota de {nt}')
  else:
    continue