""" 
1. Escreva uma função chamada square que receba um parâmetro chamado t,que é um turtle. Ela deve usar o turtle para desenhar um quadrado.
Escreva uma chamada de função que passe bob como um argumento para o
square e então execute o programa novamente.

2. Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o comprimento dos lados seja length e
então altere a chamada da função para fornecer um segundo argumento. Execute o programa novamente. Teste o
seu programa com uma variedade de valores para length.

3. Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe 
um polígono regular de n lados.

Dica: os ângulos exteriores de um polígono regular de n lados são 360/ngraus.

4. Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e desenhe um círculo aproximado
ao chamar polygon com um comprimento e número de lados adequados. Teste a sua função com uma série de valores de r.

Dica: descubra a circunferência do círculo e certifique-se de que length * n = circumference.

5. Faça uma versão mais geral do circle chamada arc, que receba um
parâmetro adicional de angle, para determinar qual fração do círculo deve
ser desenhada. angle está em unidades de graus, então quando angle=360, o
arc deve desenhar um círculo completo.
"""

import turtle
bob = turtle.Turtle()


def square(t, length: int, pixels: int):
    for i in range(n):
        t.fd(length)    # Avança 'length' pixels
        t.lt(pixels)    # Vira à esquerda com ângulo adequado
    turtle.mainloop()    


def polygon(t, n,length: int):
    angulo = 360/n
    for i in range(n):
        t.fd(length)    # Avança 'length' pixels
        t.lt(angulo)    # Vira à esquerda com ângulo adequado
    turtle.mainloop()    


def circle(t,n,raio):
    """_summary_
    Args:
    t -- metodo turtle
    n -- número de lados do polígono (quanto maior, mais arredondado)
    raio -- raio do círculo    
    """
    valor_pi = 3.1416
    length = (2 * valor_pi * raio)/n 
    polygon(t=t,n=n, length=length)



def arc(t,n,raio, angle):

    valor_pi = 3.1416
    circunferencia = (2 * valor_pi * raio)
    fracao = angle/360
    comprimento_arco = fracao * circunferencia
    length = comprimento_arco / n
    curva_por_passo = angle/n

    for i in range(n):
        t.fd(length)    
        t.lt(curva_por_passo)    


   




square(bob, 80, 100)
polygon(bob,10,100)
circle(bob, 120,100)
arc(bob,90,100,180)