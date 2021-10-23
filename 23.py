num = int(input('Digite um numero: ')) # 5505

u = num // 1 % 10 # 5
d = num // 10 % 10 # 0
c = num // 100 % 10 # 5
m = num // 1000 % 10 # 5

print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(m, c, d, u)) # 5, 5, 0, 5