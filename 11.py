A = int(input('Insira a largura da parede: ')) # 5
B = int(input('Insira a altura da parede: ')) # 5
area = A * B
tinta = 2

print('Área: {}m^2\nQuantidade de litro de tinta necessária para pintar a parede: {}l'.format(area, area/tinta)) # 25m^2, 12.5l