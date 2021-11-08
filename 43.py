peso = float(input('Digite seu peso (KG): ')) # 53.3
altura = float(input('Digite sua altura (M): ')) # 1.71

imc = peso / (altura ** 2)
print('\nSeu IMC é {:.2f}, e sua classificação é '.format(imc), end='') # ABAIXO DO PESO!

if imc < 18.5:
  print('ABAIXO DO PESO!')
elif imc >= 18.5:
  print('PESO NORMAL!')
elif imc >= 25:
  print('SOBREPESO!')
elif imc >= 30:
  print('OBESIDADE!')
elif imc > 40:
  print('OBESIDADE MÓRBIDA!')