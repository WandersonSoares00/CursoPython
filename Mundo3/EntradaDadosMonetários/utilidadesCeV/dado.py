
def leiaDinheiro(msg):
    vermelho = '\033[1;91m'
    padrao = '\033[0;0m'
    temp = ''
    while True:
        temp = input(msg).replace(',', '.').strip()
        if temp.isalpha() or temp == '':
            print(vermelho + f'Erro: \"{temp}\" não é um valor válido em dinheiro!' + padrao)
        else: 
            if temp.count('.') < 2 and temp.replace('.', '').isnumeric():
                val = float(temp)
                return val
            else:
                print(vermelho + f'Erro: \"{temp}\" não é um valor válido em dinheiro!' + padrao)

