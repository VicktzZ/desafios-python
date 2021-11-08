a = int(input('Digite o primeiro valor: ')) # 1000
b = int(input('Digite o segundo valor: ')) # 23
c = int(input('Digite o terceiro valor: ')) # 5402

if a >= b and a >= c:
  maior = a
elif b >= a and b >= c:
  maior = b
elif c >= a and c >= b:
  maior = c

if a <= b and a <= c:
  menor = a
elif b <= a and b <= c:
  menor = b
elif c <= a and c <= b:
  menor = c

print('\nO \033[32mMAIOR\033[m valor digitado foi: {}'.format(maior)) # 5402
print('O \033[31mMENOR\033[m valor digitado foi: {}'.format(menor)) # 23
