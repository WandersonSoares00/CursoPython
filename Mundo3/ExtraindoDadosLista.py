#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
cont = 0
#Solução sem o método sort
while True:
    valor = int(input(f'Informe o {cont + 1}° valor da lista: '))
    if cont == 0 or valor <= lista[-1]:
        lista.append(valor)
    else:
    #Procura um valor maior que a entrada na lista, no momento em que achar, se insere antes dele
        for pos in range(len(lista)):
            if valor >= lista[pos]:
                lista.insert(pos, valor)
                break
    continua = input('Continuar? [S\\N] ')
    if continua[0].upper() == 'N':
        break
    cont += 1
print(f'\nForam informados {cont + 1} valores na lista.')
print(f'Lista decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi informado e está na lista.\n')
else:
    print('O valor 5 não foi informado e não está na lista.\n')
