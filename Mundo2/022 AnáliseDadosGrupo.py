"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
"""
mais18 = menos20 = homem = 0

while True:
    idade = int(input('Entre a idade: '))
    sexo = input('Entre o sexo: [M/F] ').upper()
    while sexo != 'M' and sexo != 'F':
        sexo == input('Entre um sexo valido: [M/F] ').upper()
    if idade > 18:
        mais18 += 1
    if sexo == 'F':
        if idade < 20:
            menos20 += 1
    else:
        homem += 1
    continua = input('Quer continuar? [S/N] ').upper()
    while continua not in 'SIMNAO':
        continua = input('Quer continuar? [S/N] ').upper()
    if continua in 'NAO':
        break
print(f'\nDados recebidos. Ao todo foram:\n{mais18} pessoas com mais de 18 anos.')
print(f'{menos20} mulheres com menos de 20 anos.\n{homem} homens cadastrados.')
