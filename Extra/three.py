'''
Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
'''

diaria_hotel = 150
valor_gasolina = 5
cidades = ['Salvador', 'Fortaleza', 'Natal', 'Aracaju']
gastos_gerais = [200, 400, 250, 300] # por cidade, respectivamente
distancia_cidades = [850, 800, 300, 550]
pergunta_dias = int(input('Quantos dias você passará na viagem: '))

def calculando_viagem(diaria_hotel, valor_gasolina, cidades, gastos_gerais, distancia_cidades, pergunta_dias):
  # viagem de 3 dias para Salvador, partindo de Recife. Considerando ida e volta de carro.
  total_hotel = pergunta_dias * diaria_hotel
  total_gasolina = (14 / distancia_cidades[1]) * valor_gasolina
  total_gastos_gerais = pergunta_dias * gastos_gerais[1]
  total_tudo = total_hotel + total_gasolina + total_gastos_gerais
  return print(f'Gasto Total para a cidade de: {cidades[1]}: R$ {total_tudo}')

calculando_viagem(diaria_hotel, valor_gasolina, cidades, gastos_gerais, distancia_cidades, pergunta_dias)

