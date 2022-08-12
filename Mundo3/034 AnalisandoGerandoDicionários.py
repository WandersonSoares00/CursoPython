#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
#retornar um dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)
#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(*n, sit = False):
    """
    -> Função que analisa as notas e gera, a partir da entrada, informações sobre o desempenho da turma
    Parâmetros:
    n: Notas dos alunos
    sit: situação da turma (opcional)
    *return: dicionário com informações da turma cujas notas foram informadas
    """
    desempenho = dict()
    desempenho['Quantidade'] = len(n)
    desempenho['Maior nota'] = max(n)
    desempenho['Menor nota'] = min(n)
    m = sum(n) / desempenho['Quantidade']
    desempenho['Média'] = m
    if sit:
        if desempenho['Média'] >= 7:
            desempenho['Situação'] = 'BOA'
        elif desempenho['Média'] >= 6:
            desempenho['Situação'] = 'RAZOÁVEL'
        else:
            desempenho['Situação'] = 'RUIM'
    return desempenho


print(notas(7, 6.5, 9.0, 7.5, 10))
print(notas(9, 4.3, 7, 6, sit = True))
help(notas)