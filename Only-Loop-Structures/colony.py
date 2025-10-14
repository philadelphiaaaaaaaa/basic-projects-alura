'''
Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
'''

# bactéria A ---> taxa de crescimento de 3% (iniciando com 4 elementos)
# bactéria B ---> taxa de crescimento de 1,5% (iniciando com 10 elementos)

colony_A = 4
colony_B = 10
counter = 1

taxa_A = 0.03
taxa_B = 0.015

while colony_A <= colony_B:
  colony_A += taxa_A
  counter += 1
  
print('')
print('Com taxa de crescimento de 3% por dia, finalmente a colônia de bactérias A alcançou a colônia de bactérias B!')
print(f'Foram necessários {counter} dias para alcançar a colônia de bactérias B. O valor de elementos atingido pela colônia A foi de {colony_A}.')

