#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
#de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
#OBRIGATÓRIO nas eleições.

def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    print(f'Uma pessoa que nasceu no ano de {nasc} tem {idade} anos e seu voto é ', end='')
    if idade < 16:
        return 'NEGADO'
    elif (idade >= 16 and idade < 18) or idade >= 65:
        return 'OPCIONAL'
    
    elif idade >= 18 and idade <= 65:
        return 'OBRIGATÓRIO'


print(voto(2010))
print(voto(2005))
print(voto(1985))
print(voto(1950))
