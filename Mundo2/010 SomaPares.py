#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
#forem pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0
for i in range(1, 7, +1):
	v = int(input('Valor {}: ' .format(i)))
	if v % 2 == 0:
		s = s + v
print('A soma eh: {}' .format(s))
