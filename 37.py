num = int(input('Digite um número inteiro: ')) # 1257

print('\nAgora escolha um método de conversão para o número inserido:\n[0] Binário\n[1] Octal\n[2] Hexadecimal')
escolha = int(input('Sua opção: ')) # 2

def converter(conv, method):
  print('\n{} convertido para {}: {:{method}}'.format(num, conv, num, method=method))

if escolha == 0:
  converter('Binário', 'b')
elif escolha == 1:
  converter('Octal', 'o')
else:
  converter('Hexadecimal', 'x') # 1257 convertido para Hexadecimal: 4e9