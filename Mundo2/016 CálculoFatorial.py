#Faça um programa que leia um número qualquer e mostre o seu fatorial.

v = int(input('Informe o valor: '))
resultado = 1
i = 1
for i in range(v, 0, -1):
    print('{} x' .format(i), end= ' ')
    resultado *= i
print('{}! = {}' .format(i - 1, resultado))
