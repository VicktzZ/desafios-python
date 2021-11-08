viagem = int(input("Digite em quilômetros qual foi a distância da viagem (KM): ")) #1200

if viagem < 200:
  preco_viagem = viagem * 0.5
else:
  preco_viagem = viagem * 0.45

print('Preço da viagem: R${:.2f}'.format(preco_viagem)) # R$540.00