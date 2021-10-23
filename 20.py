from random import shuffle

arr = [0, 1, 2, 3]

arr[0] = input('Digite o nome do primeiro aluno: ') # Vitor
arr[1] = input('Digite o nome do segundo aluno: ') # Hugo
arr[2] = input('Digite o nome do terceiro aluno: ') # Rodrigues
arr[3] = input('Digite o nome do quarto aluno: ') # Santos

shuffle(arr)

print('Ordem dos alunos apresentada: {}'.format(arr)) # ['Hugo', 'Rodrigues', 'Santos', Vitor]