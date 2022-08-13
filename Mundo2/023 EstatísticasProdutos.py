"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.

"""
valor = int(input('Digite o valor a ser sacado: R$ '))

qtd_ced50 = valor // 50
valor = valor - (qtd_ced50 * 50)
qtd_ced20 = valor // 20
valor = valor - (qtd_ced20 * 20)
qtd_ced10 = valor // 10
valor = valor - (qtd_ced10 * 10)
qtd_ced1 = valor

print(f'Voce vai receber: {qtd_ced50} cedulas de 50 R$')
print(f'Voce vai receber: {qtd_ced20} cedulas de 20 R$')
print(f'Voce vai receber: {qtd_ced10} cedulas de 10 R$')
print(f'Voce vai receber: {qtd_ced1} moedas de 1 R$')
