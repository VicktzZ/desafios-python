vel = int(input('Qual a velocidade do veículo (KM/h)?: ')) # 120

if vel > 80:
  print('Veículo acima do limite de velocidade! MULTA de R${}.'.format((vel-80) * 7)) # R$280
else:
  print('Veículo dentro do limite de velocidade :)')

