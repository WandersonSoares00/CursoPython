#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
#pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

print('*'* 14, 'Tabuada', '*'* 14)
while True:
    print('Digite um valor para ver sua tabuada.\nInforme um valor negativo para sair.\n')
    n = int(input('Entrada: '))
    if n < 0:
        break
    for i in range(11):
        print(f'{n} x {i} = {n * i}')
