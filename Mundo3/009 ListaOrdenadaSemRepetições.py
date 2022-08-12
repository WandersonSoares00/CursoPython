#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for i in range(5):
    valor = int(input('Informe o valor: '))
    if i == 0 or valor >= lista[-1]:
        lista.append(valor)
    else:
    #Pecorre a lista até que chegue em um valor menor que a entrada, nesse momento, se insere antes desse valor.
        for pos in range(len(lista)):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
print(f'Lista ordenada: {lista}')
