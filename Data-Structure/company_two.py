'''
Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
'''

spent_values = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
spent_new_values = []

for value in spent_values:
  if value > 3000:
    spent_new_values.append(value)
  else:
    continue

order_new_values = spent_new_values.sort() # para retornar em ordem crescente: sort(reverse=True)
quantity_values_original = len(spent_values)
quantity_values_new = len(spent_new_values)
percent_new_values = (quantity_values_new / quantity_values_original) * 100

print(
f'''
Foram realizadas {quantity_values_new} compras acima de 3000 reais com porcentagem de {percent_new_values}% em relação a quantidade total que são de {quantity_values_original} compras.
'''
)