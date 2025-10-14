'''
Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

    Para variação acima de 20%: bonificação para o time de vendas.
    Para variação entre 2% e 20%: pequena bonificação para time de vendas.
    Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
    Para bonificações abaixo de -10%: corte de gastos.
'''

get_quantity_2022 = int(input('[1] Digite a quantidade de vendas realizadas no ano de 2022: '))
get_quantity_2023 = int(input('[2] Digite a quantidade de vendas realizadas no ano de 2023: '))
calculating_variation = ((get_quantity_2023 - get_quantity_2022) / get_quantity_2022) * 100

if calculating_variation > 20:
  print(f'[INFO] Felicidades, bonificação para o time de vendas. Variação: {calculating_variation}%')
if 2 <= calculating_variation <= 20:
  print(f'[INFO] Felicidades, pequena bonificação lhes alcançou. Variação: {calculating_variation}%')
if -10 <= calculating_variation <= 2:
  print(f'[INFO] Começaremos um planejamento político de incentivo às vendas. Variação: {calculating_variation}%')
if calculating_variation < -10:
  print(f'[INFO] Haverá corte de gastos, a variação ficou muito baixa. Variação: {calculating_variation}%')

