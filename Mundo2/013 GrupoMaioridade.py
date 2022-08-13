#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
#ainda não atingiram a maioridade e quantas já são maiores.

qMenor = 0
qMaior = 0
for i in range(1, 8, +1):
	data = int(input('Data de nascimento em anos %d: ' %i))
	if (2022 - data) >= 18:
		qMaior += 1
	else:
		qMenor += 1
print('%d' %qMaior, ' pessoas sao maiores de idade e %d nao sao menores de idade.' %qMenor)
