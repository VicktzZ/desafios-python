from datetime import date
ano = int(input('Digite um ano (digite "0" para usar o ano atual): ')) # 1900
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 & ano % 100 != 0 | ano % 400 == 0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} NÃO é Bissexto.'.format(ano)) # O ano 1900 NÃO é Bissexto.