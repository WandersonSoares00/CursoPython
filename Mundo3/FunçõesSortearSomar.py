#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
#a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteia(vals):
    for i in range(5):
        vals.append(randint(0, 10))
    print(f'\nOs valores sorteados foram: {vals}')


def somaPar(vals):
    soma = 0
    for i in range(5):
        if vals[i] % 2 == 0:
            soma += vals[i]
    print(f'\nA soma dos valores pares é {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
