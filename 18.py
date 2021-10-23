from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo para cálculo: ')) # 30

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Seno: {:.2f}\nCosseno {:.2f}\nTangente: {:.2f}'.format(seno, cosseno, tangente)) # 0.50, 0.87, 0.58