#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
#analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
pilha = []
exp = input('Informe uma expressão matemática com parênteses: ')
for caractere in exp:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        elif len(pilha) == 0:
            pilha.append(caractere)
            break
if len(pilha) == 0:
    print(f'A expressão {exp} é válida.')
else:
    print(f'A expressão {exp} é inválida.')
