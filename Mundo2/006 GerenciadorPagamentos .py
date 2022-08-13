"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""
valor = float(input('Informe o valor da compra: '))

n = int(input('''Informe a opcao de pagamento:
    [1] A vista(10% de desconto)
    [2] A vista no cartao de credito(5% de desconto)
    [3] 2x no cartao de credito(Valor integral)
    [4] 3x ou mais no cartao(20% de juros)\n
'''))

if n == 1:
    print('A sua compra de {} R$ vai custar {} R$ com {} R$ de desconto' .format(valor, 90/100 * valor, 1/10 * valor))
elif n == 2:
    print('A sua compra de {} R$ vai custar {} R$ com {} R$ de desconto'.format(valor, 95/100 * valor, 5/100 * valor))
elif n == 3:
    print('A sua compra de {} R$ vai custar duas parcelas de {} R$'.format(valor, valor/2))
elif n == 4:
    print('A sua compra de {} R$ vai custar {} R$ no total.' .format(valor, valor*12/10))
else:
    print('\033;34mOpcao de pagamento invalida.')
