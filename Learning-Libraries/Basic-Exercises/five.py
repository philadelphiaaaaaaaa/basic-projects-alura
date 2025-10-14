'''
Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar. 
'''

from math import pi, pow

raio = float(input('Digite o raio do jardim: '))
area = pi * pow(raio, 2)
price = area * 25.00

print(f'Você precisará pagar um total de {price} reais.')