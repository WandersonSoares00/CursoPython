#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
i = 0
while True:
    valor = int(input(f'Valor da posição {i + 1}: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print(f'O valor {valor} já está listado. Tente novamente.')
        continue
    continua = input('Continuar? [S\\N] ')
    if continua[0].upper() == 'N':
        break
    i += 1
lista.sort()
print(f'Lista em ordem crescente: {lista}')
