shopping_price = float(input('Qual o preço das compras?: R$'))
print('\nQual a foram de pagamento?:\n[0] À vista dinheiro/cheque\n[1] À vista cartão\n[2] 2x no cartão\n[3] 3x ou mais no cartão')
option = int(input('Sua opção: '))

if option == 0:
  shopping_price = shopping_price * 0.9
  print('À vista em dinheiro/cheque o valor final receberá 10% de desconto: R${:.2f}'.format(shopping_price))
elif option == 1:
  shopping_price = shopping_price * 0.95
  print('À vista no cartão o valor final receberá 5% de desconto: R${:.2f}'.format(shopping_price))
elif option == 2:
  print('O valor parcelado em 2x será de: R${:.2f}.'.format(shopping_price/2))
else:
  option = int(input('Deseja parcelar em quantas vezes no cartão?: '))
  if option < 3:
    option = 3
  shopping_price = (shopping_price * 1.2) / option
  print('Parcelando em {}x com 20% de juros o preço final será de: R${:.2f}.'.format(option, shopping_price))