#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = float(input('Informe o primeiro termo: '))
r = float(input('Informe a razao da PA: '))
s = 0
for i in range(0, 10, +1):
	s = a1 + (i * r)
	print(s , end = ',  ')
print('FIM')
