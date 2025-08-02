""" 9.4 Pessoas atendidas: Comece com o seu programa do Exercício 9.1 (página 208).
Adicione um atributo chamado number_served com um valor default de 0. Crie uma
instância chamada restaurant a partir dessa classe. Exiba o número de clientes que o
restaurante atendeu e, em seguida, altere este valor e o exiba novamente.
Adicione um método chamado set_number_served() que possibilita definir o número de
clientes atendidos. Chame esse método com um novo número e exiba mais uma vez o
valor.

Adicione um método chamado increment_number_served(), o qual possibilita aumentar
o número de clientes atendidos. Chame esse método com qualquer número que quiser
e que possa representar quantos clientes foram atendidos em, digamos, um dia de
atividade comercial.

9.5 Tentativas de login: Adicione um atributo chamado login_attempts à sua classe
User do Exercício 9.3 (página 209). Crie um método chamado
increment_login_attempts() que incrementa o valor de login_attempts em 1. Crie outro
método chamado reset_login_attempts() que redefine o valor de login_attempts para 0.
Crie uma instância da classe User e chame increment_login_attempts() diversas vezes.
Exiba o valor de login_attempts para verificar que foi incrementado corretamente e, em
seguida, chame reset_login_attempts(). Exiba login_attempts novamente a fim de ter
certeza de que foi redefinido para 0.
"""

class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
             
    
    def describe_restaurant(self):
        """ Exibre informações do restaurante. """
        print(f'Nome: {self.restaurant_name}')
        print(f'Tipo de restaurante: {self.cuisine_type}')
    
    
    def open(self):
        """ Exibe uma mensagem sinalizando que o restaurante está aberto."""
        print(f'{self.restaurant_name} está aberto')
    
    
    def describe_number_served(self):
        print(f'Qtd de atendimento: {self.number_served}')
    
    
    
    def increment_number_served(self, quantity):
        self.number_served += quantity
        

    def set_number_served(self,quantity):
        self.number_served = quantity         



class User:
    
    def __init__(self,first_name,last_name,documento, idade):
        self.first_name = first_name
        self.last_name  = last_name
        self.documento  = documento
        self.idade      = idade
        self.login_attempts = 0


    def greet_user(self):
        full_name = f'{self.first_name} {self.last_name}'.title()
        print(f'Seja bem-vindo {full_name}')


    def describe_login_attempts(self):
        """ Informa o valor de login_attempts."""

        print(f'QTD logins : {self.login_attempts}')

    def increment_login_attempts(self):
        """ incrementa o valor de login_attempts em 1 """
        self.login_attempts += 1
    
    
    def reset_login_attempts(self):
        """ redefine o valor de login_attempts para 0 """
        self.login_attempts = 0

"""
restaurant = Restaurant('BK','delivery')

restaurant.describe_number_served()
restaurant.number_served = 1
restaurant.describe_number_served()
restaurant.set_number_served(15)
restaurant.describe_number_served()
restaurant.increment_number_served(2)        
restaurant.describe_number_served()


user1 = User('matheus','santos','00028922',15)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.describe_login_attempts()

user1.reset_login_attempts()
user1.describe_login_attempts()
"""