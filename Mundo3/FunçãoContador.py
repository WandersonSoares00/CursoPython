#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
#início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
from time import sleep

def contador(inic, fim, passo):
    print(f'\ncontagem de {inic} até {fim}, de {abs(passo)} em {abs(passo)}:')
    sleep(1.5)
    passo = abs(passo)
    if passo == 0:
        passo = 1
    if inic > fim:
        passo *= -1
        fim -= 1
    elif fim > inic:
        fim += 1
    for cont in range(inic, fim, passo):
        print(cont, end = ', ', flush = True)
        sleep(0.4)
    print(' FIM')


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('\nContagem personalizada.\nInício: '))
final = int(input('Fim: '))
pas = int(input('Passo: '))
contador(inicio, final, pas)
