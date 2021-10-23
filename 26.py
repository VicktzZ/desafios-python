string = input('Digite uma frase: ').strip() # o rato roeu a roupa do rei de roma
print('\nA letra "A" aparece {} vezes;'.format(string.upper().count('A'))) # 4
print('A primeira letra "A" está na posição {};'.format(string.upper().find('A') + 1)) # 4
print('A ultima letra "A" está na posição {}.'.format(string.upper().rfind('A') + 1)) # 34
