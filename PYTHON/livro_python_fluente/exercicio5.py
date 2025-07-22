"""
Exercício 5.1
O módulo time fornece uma função, também chamada time, que devolve a Hora Média de Greenwich na “época”, que é um 
momento arbitrário usado como ponto de referência. Em sistemas UNIX, a época é primeiro de janeiro de 1970.
    >> import time
    >> time.time()
    1437746094.5735958
Escreva um script que leia a hora atual e a converta em um tempo em horas,minutos e segundos, mais o número de dias desde a época.

Exercício 5.2
O último teorema de Fermat diz que não existem números inteiros a, b e c tais que a**n + b**n == c**n para quaisquer valores 
de n maiores que 2.

1. Escreva uma função chamada check_fermat que receba quatro parâmetros –a, b, c e n – e verifique se o teorema de Fermat se mantém.
Se n for maior que 2 e a**n + b**n == c**n o programa deve imprimir, “Holy smokes, Fermat was wrong!”
Senão o programa deve exibir “No, that doesn’t work.”

2. Escreva uma função que peça ao usuário para digitar valores para a, b, c e n, os converta em números inteiros e use check_fermat
para verificar se violam o teorema de Fermat.
"""

from time import gmtime, time

tempo_em_segundos = time()

def segundos_para_data(seconds: float):
    data_convertida = gmtime(seconds)
    
    print(f'Segundos: {seconds}')
    print(data_convertida)
    
    
    
def check_fermat (a: int, b: int, c: int, n: int) -> str:    
    if n <= 2:
        print('the value of N is less than or equal to 2, Fermat is correct.')

    else:
        soma_ab    =  (a ** n) + (b ** n)
        valor_de_c = c ** n
            
        if soma_ab ==  valor_de_c:
            print('Holy smokes,Fermat was wrong!')
        else:
            print('No, that doesn’t work.')


def input_values_fermat():
    a = int(float(input('Informe o valor de A: ')))
    b = int(float(input('Informe o valor de B: ')))
    c = int(float(input('Informe o valor de C: ')))
    n = int(float(input('Informe o valor de N: ')))        
    
    check_fermat(a,b,c,n)


segundos_para_data(tempo_em_segundos)
input_values_fermat()