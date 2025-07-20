"""
Escreva uma função chamada right_justify, que receba uma string chamada s
como parâmetro e exiba a string com espaços suficientes à frente para que a
última letra da string esteja na coluna 70 da tela:

1. Digite este exemplo em um script e teste-o.

2. Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e chame a função duas vezes, 
passando o valor como um argumento.

3. Copie a definição de print_twice que aparece anteriormente neste capítulo no seu script.

4. Use a versão alterada de do_twice para chamar print_twice duas vezes, passando 'spam' como um argumento.

5. Defina uma função nova chamada do_four que receba um objeto de função
e um valor e chame a função quatro vezes, passando o valor como um
parâmetro.
"""

def right_justify(valor_texto: str = '' ) -> str:
   
   tamanho_do_texto =  len(valor_texto) 
   quantidade_de_espacamento = 70 - tamanho_do_texto
   texto_com_espacamento = (' '*quantidade_de_espacamento)+valor_texto
   
   print(texto_com_espacamento)
   


#right_justify(valor_texto='monty')
#right_justify(valor_texto='enginners')   
#right_justify(valor_texto='six')   


def do_twice(function, value):
    function(value)
    function(value)


def print_value(value):
    print(value)


def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(function, value):
    do_twice(function,value)
    do_twice(function,value)
    

#do_twice(print_value, 'jorge')
# do_twice(print_twice, 'spam')    
#do_four(print_value, 'truco')





""" 
                    Exercício 3.3
1. Escreva uma função que desenhe uma grade como a seguinte:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

2. Escreva uma função que desenhe uma grade semelhante com quatro linhas
e quatro colunas.
"""
    
def linha_tracejada(caractere_separador: str = '', qtd_linhas: int=1):
    texto = f'{caractere_separador} - - - - '
    print((texto*qtd_linhas)+caractere_separador)
    
    
def linha_com_espaco(caractere_separador: str = '',qtd_linhas: int=1):
    texto = f'{caractere_separador}         '
    print((texto*qtd_linhas)+caractere_separador)
        

def desenho_da_grade(qtd_linhas: int = 2):
    qtd_linhas = qtd_linhas - 1
    for i in range(0,qtd_linhas):
        linha_tracejada('+',qtd_linhas)
        linha_com_espaco('|',qtd_linhas)
        linha_com_espaco('|',qtd_linhas)
        linha_com_espaco('|',qtd_linhas)
    linha_tracejada('+',qtd_linhas)


desenho_da_grade(qtd_linhas=3)
"""
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""
desenho_da_grade(qtd_linhas=4)
"""
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
"""