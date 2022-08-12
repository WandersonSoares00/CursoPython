#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
dados = list()
info = list()
maior = menor = 0
while True:
    info.append(input('Informe seu nome : '))
    info.append(float(input('Informe seu peso: ')))
    if len(dados) == 0:
        maior = menor = info[1]
    else:
        if info[1] > maior:
            maior = info[1]
        if info[1] < menor:
            menor = info[1]
    dados.append(info[:])
    info.clear()
    continua = input('Quer continuar? [S\\N] ').upper()
    if continua[0] == 'N':
        break
print(f'No total, foram {len(dados)} pessoas cadastradas.')
print(f'As pessoas com maior peso foram ', end = ' ')
for pessoa in dados:
    if pessoa[1] == maior:
        print(pessoa[0], end=' ')
print()
print(f'As pessoas com menor peso foram ', end = ' ')
for pessoa in dados:
    if pessoa[1] == menor:
        print(pessoa[0], end=' ')
print()
