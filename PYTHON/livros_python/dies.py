"""
9.13 Dados: Crie uma classe Die com um atributo chamado sides, que tem um valor
default de 6. Crie um método chamado roll_die() que exiba um número aleatório entre
1 e o número de lados que o dado tem. Crie um dado com 6 lados e jogue-o 10 vezes.
Crie um dado com 10 lados e um com 20 lados. Jogue cada dado 10 vezes.

9.14 Loteria: Crie uma lista ou tupla contendo uma série de 10 números e 5 letras.
Selecione aleatoriamente 4 números ou letras da lista e exiba uma mensagem
informando que qualquer bilhete que corresponda a esses 4 números ou letras ganha
um prêmio.

9.15 Análise de loteria: Você pode usar um loop a fim de verificar a dificuldade de
alguém ganhar o tipo de loteria que acabou de modelar. Crie uma lista ou tupla
chamada my_ticket. Escreva um loop que continue analisando números até seu bilhete
ganhar. Exiba uma mensagem informando quantas vezes o loop teve que ser executado
até sortear um bilhete vencedor.
"""
from random import randint, Random, choice

class Loteria:
    def __init__(self):
        self.valores = (1,2,3,4,5,6,7,8,9,15,'A','K','M','L','S')
        self.bilhete = []
        self.meu_bilhete = []
        
    
    def bilhete_sorteado(self):
        self.bilhete = []
        i = 0
        while i < 4:            
            valor_sorteado = choice(self.valores)
            self.bilhete.append(valor_sorteado)
            i+=1
        print(f'qualquer bilhete que corresponda a esses 4 números ou letras ganhaum prêmio.  {self.bilhete}')
    
    
    def my_ticket(self):
        
        vcontador = 0
        ind_sorteado = True
        while ind_sorteado:
            vcontador +=1
            self.meu_bilhete = []    
            
            i = 0
            while i < 4:            
                valor_sorteado = choice(self.valores)
                self.meu_bilhete.append(valor_sorteado)
                i+=1
            
            if self.meu_bilhete == self.bilhete:
                print()
                print(f'Meu bilhete {self.meu_bilhete} foi sorteado após {vcontador} tentativas.')
                ind_sorteado = False
    
class Die:    
    def __init__(self, sides = 6):
        self.sides = sides


    def roll_die(self):
        value = randint(1, self.sides)
        print(f'- {value}')
        


die = Die()
die2 = Die(10)

for i in range(1,11):  
    die.roll_die()        

for i in range(1,21):
    die2.roll_die()        

loteria = Loteria()


loteria.bilhete_sorteado()
loteria.my_ticket()