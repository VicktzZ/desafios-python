primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
PA = []

for i in range(1, 11):
    PA.append(primeiroTermo + (i - 1) * razao)

print(''.join(str(PA)))