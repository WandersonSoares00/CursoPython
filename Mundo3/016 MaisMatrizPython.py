#Aprimore o desafio Matriz em Python, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[], [], []]
somat_par = soma3c = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Informe um valor inteiro para [{i},{j}]: ')))
maior = matriz[1][0]
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end= '')
        if matriz[i][j] % 2 == 0:
            somat_par += matriz[i][j]
        if j == 2:
            soma3c += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    print()

print(f'A soma de todos os valores pares digitados é igual a {somat_par}')
print(f'A soma dos valores da terceira coluna é igual a {soma3c}')
print(f'O maior valor da segunda linha é o {maior}')
