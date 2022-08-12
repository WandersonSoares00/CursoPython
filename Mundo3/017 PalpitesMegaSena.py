#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
temp = list()
qtd = int(input('Informe quantos jogos vão ser gerados: '))
jogos = [[]] * qtd

for i in range(qtd):
    j = 0
    while j < 6:
        aleatorio = randint(1, 60)
        if aleatorio not in temp:
            temp.append(aleatorio)
            j += 1
    jogos[i] = temp[:]
    temp.clear()

print('\nOs seguintes jogos foram gerados:\n')
for i in range(qtd):
    print(f'\tJogo {i + 1}: ', end='')
    sleep(1)
    for j in range(6):
        print(f'|{jogos[i][j]:^2}| ', end='')
    print('\n      ', '**' * 20)
