soma = 0

for i in range(6):
    num = int(input(f'Digite o número {i}: '))
    
    if num % 2 == 0:
        soma += num

print('\n' + str(soma))