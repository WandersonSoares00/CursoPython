#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
#mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = tupla[0]
menor = tupla[1]
print(f'A tupla gerada é: {tupla}\n')
for valor in tupla:
    if valor > maior:
        maior = valor
    if valor  < menor:
        menor = valor
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
