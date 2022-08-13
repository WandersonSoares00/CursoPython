#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Informe um inteiro na base 10: '))
cont = 0
for i in range(1, num +1, +1):
	if num % i == 0:
	    cont += 1
	print(i, end = ', ')
print('FIM')

if cont == 2:
	print('\nPrimo! divisível por {} valores' .format(cont))
else:
	print('\nNão é primo. divisível por {} valores' .format(cont))
