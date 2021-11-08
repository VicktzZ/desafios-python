a = float(input('Digite a primeira nota: ')) # 3
b = float(input('Digite a segunda nota: ')) # 2
media = (a+b) / 2
if media >= 7:
  print('\nMédia: {:.1f}\nO aluno foi APROVADO.'.format(media))
elif media >= 5 :
  print('\nMédia: {:.1f}\nO aluno ficou de RECUPERAÇÃO.'.format(media))
else:
  print('\nMédia: {:.1f}\nO aluno foi REPROVADO.'.format(media)) # 2.5
  
