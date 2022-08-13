#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = maior = menor = 0
cont = 1

maior = menor = int(input('Digite um inteiro: '))
continua = input('Quer continuar? [s/n] ').upper().strip()[0]
soma = maior
while continua != 'N':
    n = int(input('Digite um inteiro: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    continua = input('Quer continuar? [s/n] ').upper().strip()[0]
media = soma / cont
print('\nMaior valor: {}\nMenor valor: {}\nMedia: {:.2f}' .format(maior, menor, media))
