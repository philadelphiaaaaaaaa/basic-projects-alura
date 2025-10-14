'''
verificando nota de alunos com laço de repetição:
- desejamos verificar várias notas, por exemplo, se queremos verificar uma quantidade de requisições de médias especificadas pelo usuário, faríamos da seguinte maneira:
'''

contador = 1
requisicoes_feitas = int(input("Digite a quantidade de requisições que você deseja: "))

while requisicoes_feitas <= 0:
  if requisicoes_feitas == 0:
    print('Você deve ao menos solicitar uma requisição!')
    requisicoes_feitas = int(input("Digite a quantidade de requisições que você deseja: "))
else:
  while contador <= requisicoes_feitas:
    coletando_primeira_nota = float(input("Digite a primeira nota desse(a) mesmo(a) aluno(a): "))
    coletando_segunda_nota = float(input("Digite a segunda nota desse(a) mesmo(a) aluno(a): "))
    calculo_media = (coletando_primeira_nota + coletando_segunda_nota) / 2
    print(f'A média desse(a) aluno(a) é de {calculo_media}')
    contador += 1