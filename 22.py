nome = input('Digite seu nome completo: ').strip() # Vitor Hugo Rodrigues dos Santos

print('Seu nome em letras maiusculas é: {}'.format(nome.upper())) # VITOR HUGO RODRIGUES DOS SANTOS
print('Seu nome em letras minúsculas é: {}'.format(nome.lower())) # vitor hugo rodrigues dos santos
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' '))) # 27
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome.split()[0], len(nome.split()[0]))) # Vitor, 5 letras