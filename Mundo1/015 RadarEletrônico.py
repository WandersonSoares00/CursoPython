#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
#uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual a sua km/h em? '))

if (v <= 80.00) and (v > 0.0):
    print('Boa sorte na viagem!')
elif(v > 80.0):
    multa = (v - 80.00)*7.00
    print('Multa!!\nO limite eh 80 km/h\nVoce vai ser multado em R$ %.2f' %multa)
else:
    print('Velocidade invalida.')
