'''
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Equilátero: três lados iguais;
Isósceles: dois lados iguais;
Escaleno: três lados diferentes;
'''

get_first_value = float(input('Digite o valor do primeiro lado do triângulo: '))
get_second_value = float(input('Digite o valor do segundo lado do triãngulo: '))
get_third_value = float(input('Digite o valor do terceiro lado do triângulo: '))

equilatero = get_first_value == get_second_value == get_third_value
isosceles = (get_first_value == get_second_value != get_third_value) or (get_first_value == get_third_value != get_second_value) or (get_second_value == get_third_value != get_first_value) 
escaleno = get_first_value != get_second_value != get_third_value

print('--------------------------')
print('[Informações do Triângulo]')
print('--------------------------')

if (get_first_value + get_second_value) > get_third_value:
  print('[Veracidade]: É um triângulo')
elif (get_first_value + get_third_value) > get_second_value:
  print(print('[Veracidade]: É um triângulo'))
elif (get_second_value + get_third_value) > get_first_value:
  print('[Veracidade]: É um triângulo')
else:
  print('[Veracidade]: Não é um triângulo')

if equilatero:
  print('[Tipo]: Equilátero')
elif isosceles:
  print('[Tipo]: Isósceles')
elif escaleno:
  print('[Tipo]: Escaleno')