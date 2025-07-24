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


distance_points = distance(1,2,4,6)

print(factorial(3))
