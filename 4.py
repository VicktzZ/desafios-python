A = input('Digite algo: ') # Vitor

print('Tipo:', type(A)) # <class 'str'>
print('É feito de espaços?', A.isspace()) # False
print('É um número?', A.isnumeric()) # False
print('É alfabético?', A.isalpha()) # True
print('É alfanumérico?', A.isalnum()) # True
print('É feito de letras maiúsculas?', A.isupper()) # False
print('É feito de letras minúsculas?', A.islower()) # False
print('Está capitalizada?', A.istitle()) # True