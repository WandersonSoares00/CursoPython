#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Informe um valor inteiro para [{i},{j}]: ')))
for lista in matriz:
    for j in range(3):
        print(f'[{lista[j]:^5}]', end= '')
    print()
