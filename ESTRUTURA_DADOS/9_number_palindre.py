"""
9. Número Palíndromo
Resolvido
Fácil
Tópicos
ícone de cadeado premium
Empresas
Dica
Dado um número inteiro x, retorne truese xfor umpalíndromoe falsede outra forma .

 

Exemplo 1:

Entrada: x = 121
 Saída: verdadeiro
 Explicação: 121 lê-se como 121 da esquerda para a direita e da direita para a esquerda.
Exemplo 2:

Entrada: x = -121
 Saída: falso
 Explicação: Da esquerda para a direita, lê-se -121. Da direita para a esquerda, torna-se 121-. Portanto, não é um palíndromo.
Exemplo 3:

Entrada: x = 10
 Saída: falso
 Explicação: Lê-se 01 da direita para a esquerda. Portanto, não é um palíndromo.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        left  = 0
        rigth   = len(x)-1
        while left <= rigth:
            if x[left] != x[rigth]:
                return False
            
            left += 1
            rigth -= 1
        return True
    