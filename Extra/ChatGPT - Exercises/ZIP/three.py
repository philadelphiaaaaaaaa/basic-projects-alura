'''
produtos = [lista com o nome dos produtos]
precos1 = [primeira lista com o valor dos produtos, respectivamente]
precos2 = [segunda lista com o valor dos produtos, respectivamente]
'''

produtos = ['Camiseta', 'Calça', 'Tênis', 'Boné']
precos1 = [50, 120, 300, 80]
precos2 = [55, 115, 290, 90]

# Diferença entre o final e o inicial: caso for < 0 (baixa do preço) || caso for > 0 (aumento do preço)

print('\n[VARIAÇÕES DE PREÇO]:')
indice = 1
for nome_produto, preco_desatualizado, preco_atualizado in zip(produtos, precos1, precos2):
  diferenca = preco_atualizado - preco_desatualizado
  if diferenca > 0:
    print(f'{indice}. O produto {nome_produto} sofreu um aumento de R$ {diferenca}')
    indice += 1
  elif diferenca < 0:
    print(f'{indice}. O produto {nome_produto} sofreu uma diminuição em seu preço de R$ {diferenca}')
    indice += 1
  elif diferenca == 0:
    print(f'{indice}. O produto {nome_produto} não sofreu nenhuma variação.')
    indice += 1