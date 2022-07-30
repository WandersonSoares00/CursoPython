#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços,organizando os dados em forma tabular.
tupla = ('Smartphone', 1800.00,
        'Headphone', 350.00,
        'Notebook', 2780.00,
        'Caderno', 28.50,
        'Caneta', 1.50,
        'Mouse', 18.00,
        'Livro', 47.00
        )
print('\t', '-' * 39)
print(f'\t{"Listagem de preços":^40}')
print('\t', '-' * 39)
for i in range(1, len(tupla), + 2):
    print(f'\t{tupla[i - 1]:¨<30}', f'R$ {tupla[i]:>7.2f}')
print('\t', '-' * 39)
