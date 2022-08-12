#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Informe um numero de 0 a 9999: '))

u = num%10
d = (num%100) - u
c = (num%1000) - (d + u)
um = num - (c + d + u)

print('{} = {} + {} + {} + {}' .format(num, um, c, d, u))
