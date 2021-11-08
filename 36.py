house_val = float(input('Qual o valor da casa?: ')) # 50000
buyer_sal = float(input('Qual o salário do comprador? (mensal): ')) #3270
yrs_fin = int(input('Quantos anos de financiamento?: ')) # 8

house_inst = house_val / (yrs_fin*12)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(house_val, yrs_fin, house_inst))
#Para pagar uma casa de R$50000.00 em 8 anos, a prestação será de R$520.83.

if house_inst > buyer_sal * 0.3 :
  print('De acordo com o salário, o financiamento será \033[31mNEGADO.\033[m')
else:
  print('De acordo com o salário, o financiamento será \033[32mAPROVADO.\033[m')
  # De acordo com o salário, o financiamento será APROVADO.