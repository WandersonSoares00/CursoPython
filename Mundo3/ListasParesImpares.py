#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
#crescente.
lista = [[], []]

for i in range(7):
    valor = (int(input('Informe um valor inteiro: ')))
    if valor %  2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Valores pares da lista: {sorted(lista[0])}')
print(f'Valores ímpares da lista: {sorted(lista[1])}')  
