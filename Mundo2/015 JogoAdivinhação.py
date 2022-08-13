#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 10 e peça para
#o usuário tentar descobrir qual foi o número escolhido pelo computador até acertar. O programa deverá
#mostrar no final quantos palpites foram necessários para vencer.

from random import randint
print('Vou pensar em um numero entre 0 e 10\n')
print('='*15 + 'PENSANDO...' + '='*15)

valor = randint(0, 10)

entrada = 11
jogadas = 0
while entrada != valor:
    jogadas = jogadas + 1
    entrada = int(input('\nAdivinhe o valor que eu pensei: '))
    if entrada < valor:
        print('Eh maior... Tente novamente')
    elif entrada > valor:
        print('Eh menor... Tente novamente')
print('\nVoce acertou, parabens! foram necessarias {} tentativas.' .format(jogadas))
