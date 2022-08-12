#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
val = float(input('Informe o valor: '))

print('{:.2f} com 5% de desconto é {:.2f}' .format(val, (val*0.95)))
