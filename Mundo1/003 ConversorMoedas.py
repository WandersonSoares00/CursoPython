#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
#dólares ela pode comprar.

valor = float(input('Informe o valor em reais: '))

print('{} reais corresponde a {:.2f} dolares' .format(valor, (valor/5.12)))
