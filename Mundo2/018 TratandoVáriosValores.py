#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = soma = cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um inteiro (999 para parar): '))
print('Voce digitou {} valores e a soma corresponde a {}.' .format(cont - 1, soma))
