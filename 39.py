from datetime import date

nasc = int(input('Digite o ano de nascimento do indivídiuo: ')) # 2005
idade = date.today().year - nasc

print('\nUm indivíduo que nasceu em {} tem {} anos em {}.'.format(nasc, idade, date.today().year))
#Um indivíduo que nasceu em 2005 tem 16 anos em 2021.

if idade > 18:
  print('Este indivíduo se alistou há {} ano(s).\nSeu alistamento foi em {}.'.format(idade - 18, nasc + 18))
elif idade < 18:
  print('Este indivíduo ainda não completou 18 ano(s) e não está propício ao alistamento.\nSeu alistamento será em {} ano(s) (em {}).'.format(18 - idade, date.today().year + (18 - idade)))
  # Este indivíduo ainda não completou 18 ano(s) e não está propício ao alistamento. Seu alistamento será em 2 ano(s) (em 2023).
else:
  print('Este indivíduo já tem 18 anos e está apto para o alistamento.')