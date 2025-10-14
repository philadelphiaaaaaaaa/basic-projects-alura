'''
Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
'''

get_firstvalue_list = int(input('Digite a quantidade inicial dos dados que serão avaliados: '))
get_secondvalue_list = int(input('Digite segunda a quantidade dos dados que serão avaliados: '))
quantity_list = 1


if get_firstvalue_list > get_secondvalue_list:
  for quantity_list in range(get_secondvalue_list, get_firstvalue_list + 1):
    get_principal_value_invert = int(input('Digite a nota desse dado (0 a 5): '))

    while get_principal_value_invert > 5 or get_principal_value_invert < 0:
      get_principal_value_invert = int(input('Digite a nota desse dado (0 a 5): '))
else:
  for quantity_list in range(get_firstvalue_list, get_secondvalue_list + 1):
    get_principal_value_normal = int(input('Digite a nota desse dado (0 a 5): '))

    while get_principal_value_normal > 5 or get_principal_value_normal < 0:
      get_principal_value_normal = int(input('Digite a nota desse dado (0 a 5): '))