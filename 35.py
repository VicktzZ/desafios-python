a = float(input('Digite o primeiro segmento: ')) # 5
b = float(input('Digite o seungdo segmento: ')) # 3.2
c = float(input('Digite o terceiro segmento: ')) # 8
if a < b + c and b < a + c and c < a + b:
  print('\nOs segmentos acima \033[32mPODEM\033[m formar um triângulo!') # Os segmentos acima PODEM formar um triângulo!
else:
  print('\nOs segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo!')