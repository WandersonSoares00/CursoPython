"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal(IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida

"""
h = float(input('Informe sua altura em metros: '))
p = float(input('Informe o seu peso em kg: '))

imc = p / h**2
print('O IMC e {:.2f}' .format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso normal')
elif imc <= 30:
    print('Sobrepeso, Pre-obesidade')
elif imc <= 35:
    print('Obesidade 1\nVoce tem 25% de chances de ter hipertensao e 20% de diabetes')
elif imc <= 40:
    print('Obesidade 2\nVoce tem 40% de chances de desenvolver diabetes e 50% de chances de ter doencas cardiovasculares')
elif imc > 40:
    print('Obesidade 3(Obesidade morbida)\n90% de chances de ter comorbidades. Risco de morte!!.')
