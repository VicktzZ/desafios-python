sal = float(input('Digite o salário do funcionário (R$): ')) # 2750.80
salantigo = sal
if sal < 1250:
  sal = sal + (sal*1.15)
  print('O Salário R${:.2f} teve um aumento de 15%: R${:.2f}.'.format(salantigo, sal))
else:
  sal = sal + (sal*1.1)
  print('O Salário R${:.2f} teve um aumento de 10%: R${:.2f}.'.format(salantigo, sal)) # R$5776.68
