#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
#(largura e comprimento) e mostre a área do terreno.
def area(larg, comp):
    area = larg * comp
    print(f'\nO terreno de largura {larg}m e comprimento {comp}m possui {area} m2 de área.')


comprimento = float(input('Informe o comprimento do terreno em metros: '))
largura = float(input('Informe a largura do terreno em metros: '))
area(largura, comprimento)
