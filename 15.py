dias_alg = int(input('Por quantos dias o carro foi alugado?: ')) # 14
km_perc  = float(input('Quantos quilômetros foram percorridos?: ')) # 250.50

preco_dias = 60 * dias_alg
preço_km = 0.15 * km_perc
total = preco_dias + preço_km

print('Preço por dias: R${}\nPreço por KM: R${:.2f}\nPreço do aluguel total: R${:.2f}'.format(preco_dias, preço_km, total)) # 14, 250.50, 1090.50 