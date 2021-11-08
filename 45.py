from random import randint
import time
print('+===== JOKENPO =====+')

print('\nSuas opções: ')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')

option = int(input('\nSua opção: ')) # 0
cpu_option = randint(0,2)

time.sleep(0.5)
print('\nJO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!')

if option == 0:
  print('\n+===== Você jogou Pedra! =====+')
  if cpu_option == 0:
    print('+===== O Computador jogou Pedra! =====+\n*** EMPATE ***')
  elif cpu_option == 1:
    print('+===== O Computador jogou Papel! =====+\n*** VOCÊ PERDEU! ***')
  else:
    print('+===== O Computador jogou Tesoura! =====+\n*** VOCÊ VENCEU! ***')

elif option == 1:
  print('\n+===== Você jogou Papel! =====+')
  if cpu_option == 0:
    print('+===== O Computador jogou Pedra! =====+\n*** VOCÊ VENCEU! ***')
  elif cpu_option == 1:
    print('+===== O Computador jogou Papel! =====+\n*** EMPATE ***')
  else:
    print('+===== O Computador jogou Tesoura! =====+\n*** VOCÊ PERDEU! ***')

else:
  print('\n+===== Você jogou Tesoura! =====+')
  if cpu_option == 0:
    print('+===== O Computador jogou Pedra! =====+\n*** VOCÊ PERDEU! ***')
  elif cpu_option == 1:
    print('+===== O Computador jogou Papel! =====+\n*** VOCÊ VENCEU! ***')
  else:
    print('+===== O Computador jogou Tesoura! =====+\n*** EMPATE! ***')

# +===== Você jogou Pedra! =====+
# +===== O Computador jogou Pedra! =====+
# *** EMPATE ***')