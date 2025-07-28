import math

def mysqrt(a, x=None):
    
    if x is None:
        x = 10
    y = (x + a/x) / 2

    raiz_quadrada = math.sqrt(a)
    print(f'valor Y: {y}, valor raiz: {raiz_quadrada}')
    if y == raiz_quadrada:
        return y
                
    else:
        return mysqrt(a=a, x=y)                
    

a = 50.4253
sq = math.sqrt(a)
print(sq)
print(a)