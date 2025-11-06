'''
alunos = [lista com nomes dos alunos]
nota1 = [as primeiras notas de cada aluno, respectivamente]
nota2 = [as segundas notas de cada aluno, respectivamente]

1. Calcular a média de cada aluno, somando as suas notas (Guardar em um dicionário)
2. Retornar a situação dos alunos (aprovado/reprovado)
'''

alunos = ['Ana', 'Bruno', 'Carla', 'Daniel']
notas1 = [7.0, 8.5, 6.0, 9.0]
notas2 = [8.0, 7.5, 6.5, 9.5]
media_notas = []

for primeira_nota, segunda_nota in zip(notas1, notas2):
  calcular_media = (primeira_nota + segunda_nota) / 2
  media_notas.append(calcular_media)

guardando_notas = dict(zip(alunos, media_notas))
print(guardando_notas)

for nome_aluno, nota1_aluno, nota2_aluno in zip(alunos, notas1, notas2):
  media = (nota1_aluno + nota2_aluno) / 2
  situacao = ''

  if media >= 7.0:
    situacao = 'Aprovado'
    print(f'Aluno(a): {nome_aluno} -> Situação: {situacao} -> Média: {media}')
  elif media < 7.0:
    situacao = 'Reprovado'
    print(f'Aluno(a): {nome_aluno} -> Situação: {situacao} -> Média: {media}')
