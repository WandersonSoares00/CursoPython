#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder
#30% do salário ou então o empréstimo será negado.

vcasa = float(input('Informe o valor da casa: R$ '))
sal = float(input('Qual o seu salario? R$ '))
anos = float(input('Em quantos anos voce deseja realizar o pagamento? '))

p = vcasa / (12 * anos)
if p > 30/100 * sal:
    print('\033[0;34mNegado!!')

elif p <= 30 / 100 * sal:
    print('\033[0;34mAprovado!!')
    print('Sua prestacao mensal sera igual a: {:.2f}'.format(p))
