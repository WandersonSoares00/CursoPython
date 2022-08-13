#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
#jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint
cont = 0
print('*' * 12 ,'GAME - PAR OU IMPAR', '*'* 12)
while True:
    valor = int(input('Informe o valor: '))
    aleatorio = randint(0, 10)
    paridade = input('Par ou impar? [P/I] ').upper().strip()[0]
    while paridade not in 'PARIMPAR':
        paridade = input('Par ou impar? [P/I] ').upper().strip()[0]
    if (aleatorio + valor) % 2 == 0:
        resposta = 'Par'
    else:
        resposta = 'Impar'
    if paridade == resposta[0]:
        print('\nVoce venceu!!! $$$$-Jogue novamente-$$$$\n')
        cont += 1
    else:
        print(f'\nVoce perdeu!! o valor era {aleatorio + valor} e a resposta era {resposta}')
        print(f'Voce acertou {cont} vezes seguidas.')
        break
