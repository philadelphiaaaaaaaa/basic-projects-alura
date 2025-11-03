'''
Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
'''

nomes = ['joão', 'MaRia', 'JOSÉ']
sobrenomes = ['SILVA', 'souza', 'Tavares']

def verificating_names(x, y):
  return f'{x.capitalize()} {y.capitalize()}'

result = map(verificating_names, nomes, sobrenomes)
print(list(result))