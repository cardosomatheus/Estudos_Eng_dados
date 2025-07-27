import math

def distance (x1,y1,x2,y2):
    dx = (x2 - x1) **2
    dy = (y2 - y1) **2
    desquared = dx + dy
    result = math.sqrt(desquared)
    
    return result



def factorial(n):
    if not isinstance(n,int):
        print('The value is not interger')
        return None

    if n < 0:
        return None
    
    if n == 0:
        return 1
    
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#distance_points = distance(1,2,4,6)
#print(factorial(3))


def mdc(a: int,b: int):
    """_summary_

    Args:
        a (int): primeiro valor do mdc (maximo divisor comum)
        b (int): segundo valor do mdc (maximo divisor comum)

    Returns:
        (int): retorna o MDC dos valores A e B
    """
    
    # Passo 1: Buscar os valores divisores de  A e B
    lista_valores_divisores_A = busca_valores_divisores(valor=a)
    lista_valores_divisores_B = busca_valores_divisores(valor=b)
    
    # Passo 2: comparar os elementos em comum
    mdc = 1
    for valor in lista_valores_divisores_A:
        if valor in lista_valores_divisores_B:
            mdc *= valor
            lista_valores_divisores_B.remove(valor)  # Remove o fator usado (respeita a quantidade)

    return mdc


def busca_valores_divisores (valor:int , lista_divisor: list = None, divisor: int = 2):    
    """_summary_

    Args:
        valor (int): Buscaremos os dividores desse valor até que o valor seja <= 1
        lista_divisor (list, optional): Lista do valores dividores, Defaults = None.
        divisor (int, optional): divisor inicial e não obrigatorio do processo. Default = 2

    Returns:
        _type_: lista completa dos divisore do valor informado.
    """
    if lista_divisor is None:
        lista_divisor = []

    if valor <= 1:
        return sorted(lista_divisor)    

    if valor % divisor == 0:
        valor_divido = valor // divisor
        lista_divisor.append(divisor)
        
        return busca_valores_divisores(valor=valor_divido, divisor=divisor, lista_divisor=lista_divisor)
        
    else:
        return busca_valores_divisores(valor=valor, divisor=divisor +1, lista_divisor=lista_divisor)


print(mdc(40, 72))  # 8
print(mdc(150,72))  # 6
print(mdc(158,276)) # 2
print(mdc(460,600)) # 20