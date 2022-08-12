#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever
#na tela se o usuário venceu ou perdeu.

import random
print('Vou pensar em um numero entre 0 e 5')
print('='*15 + 'PENSANDO...' + '='*15)
lista = [0, 1, 2, 3, 4, 5]
pc = random.choice(lista)
num = int(input('Tente acertar: '))

if num == pc:
    print('Acertou!!!')
else:
    print('Errouuu!!!! eu pensei no {}' .format(pc) )
print('='*20)
