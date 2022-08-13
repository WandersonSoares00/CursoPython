#Refaça o DESAFIO 002, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Tabuada de qual inteiro? '))
for i in range(0, 11, +1):
	print('{} X {} = {}' .format(n, i, i * n))
