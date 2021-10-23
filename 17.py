from math import hypot
cat_op = float(input('Insira o valor do cateto oposto: ')) # 12
cat_adj = float(input('Insira o valor do cateto adjacente: ')) # 24
print('Hipotenusa: {:.2f}'.format(hypot(cat_op, cat_adj))) # 26.83