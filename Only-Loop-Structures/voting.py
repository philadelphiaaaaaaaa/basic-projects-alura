'''
Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

    Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
    Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).

Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
'''

total_votes = 0
number_colaborator = 1
colaborator_1 = 0
colaborator_2 = 0
colaborator_3 = 0
colaborator_4 = 0

vote_null = 0
vote_nothing = 0

print(
'''
-----------------------
Instruções da Votação:
1. Para votar no primeiro colaborador candidato, digite [1]
2. Para votar no segundo colaborador candidato, digite [2]
3. Para votar no terceiro colaborador candidato, digite [3]
4. Para votar no quarto colaborador candidato, digite [4]
[NULOS] Para votar nulo, digite [5]
[BRANCO] Para votar branco, digite [6]
-----------------------
'''
)

for i in range(0, 20):
  get_vote = int(input(f'[Colaborador {number_colaborator}] Digite seu voto: '))
  if get_vote == 1:
    colaborator_1 += 1
    total_votes += 1
    number_colaborator += 1
  elif get_vote == 2:
    colaborator_2 += 1
    total_votes += 1
    number_colaborator += 1
  elif get_vote == 3:
    colaborator_3 += 1
    total_votes += 1
    number_colaborator += 1
  elif get_vote == 4:
    colaborator_4 += 1
    total_votes += 1
    number_colaborator += 1
  elif get_vote == 5:
    vote_null += 1
    total_votes += 1
    number_colaborator += 1
  elif get_vote == 6:
    vote_nothing += 1
    total_votes += 1
    number_colaborator += 1
  else:
    print('[ERRO] Número inválido, informe um dos números que foram citados.')
    number_colaborator += 1

print(
f'''
-----------------------
Informações Gerais:
- Total de votos: {total_votes}
- Votos para o Colaborador [1]: {colaborator_1}
- Votos para o Colaborador [2]: {colaborator_2}
- Votos para o Colaborador [3]: {colaborator_3}
- Votos para o Colaborador [4]: {colaborator_4}
- Votos nulos: {vote_null}
- Votos em branco: {vote_nothing}
'''
)