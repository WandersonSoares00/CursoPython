#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
#mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
lista = [0] * 5
for i in range(5):
    lista[i] = int(input(f'Informe o {i + 1}° valor: '))
maior = max(lista)
menor = min(lista)
print(f'O maior valor da lista é {maior} que está nos índices ', end='')
for i in range(5):
    if maior == lista[i]:
        print(i, end='... ')
print(f'\nO menor valor da lista é {menor} que está nos índices ', end='')
for i in range(5):
    if menor == lista[i]:
        print(i, end='... ')
