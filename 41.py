from datetime import date

nasc = int(input('Digite o ano do nascimento do atleta: ')) # 1994
ano = date.today().year
idade = ano - nasc 

print('\nO atleta tem {} anos.'.format(idade)) # 27 anos

if idade <= 9:
  print('Classificação: MIRIM.')
elif idade <= 14:
  print('Classificação: INFANTIL.')
elif idade <= 19:
  print('Classificação: JÚNIOR.')
elif idade <= 25:
  print('Classificação: SÊNIOR.')
else:
  print('Classificação: MASTER.') # Master
  