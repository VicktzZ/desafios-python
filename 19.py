from random import randint

A = input('Digite o nome do primeiro aluno: ') # Vitor
B = input('Digite o nome do segundo aluno: ') # Manuela
C = input('Digite o nome do terceiro aluno: ') # Chesko
D = input('Digite o nome do quarto aluno: ') # Luana
rand = randint(0,3)

if rand == 0:
    R = A
elif rand == 1:
    R = B
elif rand == 2:
    R = C
else:
    R = D

print('\nAluno escolhido: {}'.format(R)) # Vitor/Manuela/Chesko/Luana