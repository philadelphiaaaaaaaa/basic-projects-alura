'''
Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente.
'''

get_type_gasoline = input("[1] Qual será o tipo de gasolina? (Etanol, Diesel) ")
get_quantity_gasoline = float(input("[2] Quantos litros de gasolina? "))

if get_type_gasoline == 'Etanol':
  # preço por litro = 1.70
  # desconto de 2% por litro (até 15 litros)
  print('---------------')
  print(f'Tipo escolhido: {get_type_gasoline}')
  print(f'Litros: {get_quantity_gasoline}')

  if get_quantity_gasoline <= 15:
    print('---------------')
    print('[DESCONTO] Você ganhou um desconto de 2% por litro.')

    original_price_etanol = get_quantity_gasoline * 1.70
    calculating_disc_etanol = get_quantity_gasoline * 2
    print(f'[INFO] Preço original: R$ {original_price_etanol}')
    print(f'[INFO] Atribuição total de desconto: {calculating_disc_etanol}%')

    disc_calculated_etanol = original_price_etanol * (calculating_disc_etanol / 100)
    print(f'[INFO] Novo preço com desconto (Valor a ser pago): R$ {disc_calculated_etanol}')
  else:
    print('---------------')
    price_without_disc_etanol = get_quantity_gasoline * 1.70
    print(f'[INFO] Preço a ser pago: R$ {price_without_disc_etanol}')

if get_type_gasoline == 'Diesel':
  # preço por litro = 2.00
  # desconto de 3% por litro (até 15 litros)
  print('---------------')
  print(f'Tipo escolhido: {get_type_gasoline}')
  print(f'Litros: {get_quantity_gasoline}')

  if get_quantity_gasoline <= 15:
    print('---------------')
    print('[DESCONTO] Você ganhou um desconto de 3% por litro.')

    original_price_diesel = get_quantity_gasoline * 2.00
    calculating_disc_diesel = get_quantity_gasoline * 3
    print(f'[INFO] Preço original: R$ {original_price_diesel}')
    print(f'[INFO] Atribuição total de desconto: {calculating_disc_diesel}%')

    disc_calculated_diesel = original_price_diesel * (calculating_disc_diesel / 100)
    print(f'[INFO] Novo preço com desconto (Valor a ser pago): R$ {disc_calculated_diesel}')
  
  else:
    print('---------------')

    price_without_disc_diesel = get_quantity_gasoline * 2.00
    print(f'[INFO] Preço a ser pago: R$ {price_without_disc_diesel}')
