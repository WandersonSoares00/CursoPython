#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
#que se encontram no intervalo de 1 até 500.

s = 0
for i in range(1, 501, +2):
	if i % 3 == 0:
		print('{} + {} = {}' .format(s, i, s + i))
		s = s + i
print('\n\nA soma eh %d' %s)
