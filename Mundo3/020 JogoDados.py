#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
#sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
val_dado = {"Jogador 1" : randint(1, 6),
            "Jogador 2" : randint(1, 6),
            "Jogador 3" : randint(1, 6),
            "Jogador 4" : randint(1, 6)}

print('Jogando o dado...')
for k, v in val_dado.items():
    sleep(1)
    print(f'O {k} ficou com o valor {v}')

print('\n=============Ranking:=============')
cont = 1
for i in sorted(val_dado, key = val_dado.get, reverse= True):
    sleep(1)
    print(f'\t{cont}° lugar: {i}')
    cont += 1
