#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
#extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
numeros = []
pares = []
impares = []
while True:
    valor = int(input('Informe um valor inteiro: '))
    numeros.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    continua = input('Quer continuar? [S\\N] ')[0].upper()
    if continua == 'N':
        break
print(f'A lista de valores informados foi: {numeros}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')
