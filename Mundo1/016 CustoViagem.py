#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input())

preco = km * 0.50 if (km <= 200.00) else preco = km * 0.45

print('Gasto: {}' .format(preco))
