a = float(input('Digite o primeiro segmento: ')) # 4
b = float(input('Digite o seungdo segmento: ')) # 4
c = float(input('Digite o terceiro segmento: ')) # 3.5
if a < b + c and b < a + c and c < a + b:
  if a == b == c:
    print('\nOs segmentos acima \033[32mPODEM\033[m formar um triângulo \033[32mEQUILÁTERO\033[m!')
  elif a != b != c != a:
    print('\nOs segmentos acima \033[32mPODEM\033[m formar um triângulo \033[32mESCALENO\033[m!')
  else:
    print('\nOs segmentos acima \033[32mPODEM\033[m formar um triângulo \033[32mISÓCELES\033[m!')
    # O segmentos acima PODEM formar um triângulo ISÓCELES!
else:
  print('\nOs segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo!')