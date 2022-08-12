#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
#a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área
#de 2 metros quadrados.

l = float(input('Entre a largura em metros: '))
h = float(input('Entre a altura em metros: '))

a = l*h
tinta = a/2
print('Sua parede tem dimensao {}X{} m' .format(l, h))
print('A area eh {} metros quad\nVoce ira precisar de {} litros de tinta para pinta-la' .format(a, tinta))
