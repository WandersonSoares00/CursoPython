#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele
#ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
#alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nasc = int(input('Informe o seu ano de nascimento: '))
idade = 2022 - nasc

print('Sua idade e : %d' %idade +' anos.')
if idade > 18:
    print('Voce teve que se alistar a partir do ano {} ' .format(nasc + 18)) #ano em que completou 18 anos
    print('Se nao se alistou, CORRA!!')
elif idade < 18:
    print('Voce deve se alistar a partir do ano {}' .format(nasc + 18)) #ano em que vai completar 18 anos
    print('Se aliste imediatamente quando chegar o tempo')
else:
    print('''Voce completou 18 anos esse ano.' 
Se aliste imediatamente!!''') #nasceu em 2004 e tem 18 anos em 2022
