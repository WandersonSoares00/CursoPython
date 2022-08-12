#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt

a = float(input('Cateto a: '))
b = float(input('Cateto b: '))

h = sqrt((a**2 + b**2))

print('A Hipotenusa é igual a {}' .format(h))
