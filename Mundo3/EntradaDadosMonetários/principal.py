#Dentro do pacote utilidadesCeV que criamos no desafio TransformandoMódulosEmPacotes, temos um módulo
#chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(),
#mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadesCeV.dado import leiaDinheiro
from utilidadesCeV.moeda import resumo

valor = leiaDinheiro('Informe um valor em reais: ')
resumo(valor, 10, 25)
