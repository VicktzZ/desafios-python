from random import randint

escolhaE = randint(0,5) # 2
escolhaP = int(input('Digite um número de 0 a 5: ')) # 4 

if escolhaP == escolhaE:
    print('\nNumero escolhido pela máquina: {}'.format(escolhaE))
    print('Você VENCEU!')
else:
    print('\nNumero escolhido pela máquina: {}'.format(escolhaE)) # 2
    print('Você PERDEU!') # Você PERDEU!