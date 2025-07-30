""" 
É possível modelar quase qualquer coisa com as classes.
Começaremos escrevendo uma simples classe, Dog, para representar
um cachorro – não um cachorro específico, mas qualquer cachorro.
O que sabemos sobre a maioria dos cachorros de estimação? Bom,
todos têm um nome e uma idade. Sabemos também que a maioria
deles senta e rola. Essas duas informações (nome e idade) e esses
dois comportamentos (sentar e rolar) serão inseridos em nossa
classe Dog porque são comuns à maioria dos cachorros. Essa classe
explicará ao Python como fazer um objeto que represente um
cachorro. Após escrever nossa classe, vamos usá-la para criar
instâncias individuais,
"""


class Dog:
    """Simples tentativa de modelar um cachorro"""
    
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentado em resposta a um comando"""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simula um cachorro rolando em resposta"""
        print(f"{self.name} rolled over!")


"""
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")  

my_dog.sit()
my_dog.roll_over()      

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
"""

""" 
9.1 Restaurante: Crie uma classe chamada Restaurant. O método __init__() para
Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type. Crie um
método chamado describe_restaurant() que exiba essas duas informações e um
método chamado open_restaurant() que exiba uma mensagem sinalizando que o
restaurante está aberto.
Crie uma instância chamada restaurant a partir da sua classe. Exiba os dois atributos
individualmente e, em seguida, chame ambos os métodos.

9.2 Três restaurantes: Comece com sua classe do Exercício 9.1. Crie três instâncias
diferentes da classe e chame describe_restaurant() para cada instância.

9.3 Usuários: Crie uma classe chamada User. Crie dois atributos chamados first_name e
last_name e diversos outros atributos que normalmente são armazenados em um perfil
de usuário. Crie um método chamado describe_user() que exiba um resumo das
informações do usuário. Crie outro método chamado greet_user() que exiba um
cumprimento personalizado ao usuário.
Crie diversas instâncias que representem usuários distintos e chame ambos os métodos
para cada um.
"""

class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    
    def describe_restaurant(self):
        """ Exibre informações do restaurante. """
        print(f'Nome: {self.restaurant_name}')
        print(f'Tipo de restaurante: {self.cuisine_type}')
    
    
    def open(self):
        """ Exibe uma mensagem sinalizando que o restaurante está aberto."""
        print(f'{self.restaurant_name} está aberto')



class User:
    
    def __init__(self,first_name,last_name,documento, idade):
        self.first_name = first_name
        self.last_name  = last_name
        self.documento  = documento
        self.idade      = idade


    def greet_user(self):
        full_name = f'{self.first_name} {self.last_name}'.title()
        print(f'Seja bem-vindo {full_name}')


restaurant = Restaurant('BK','delivery')
restaurant2 = Restaurant('Subway','delivery')
restaurant3 = Restaurant('Japa','delivery')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.open()        
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


user1 = User('matheus','santos','00028922',15)
user2 = User('marcus','medeiro','00289562',56)
user3 = User('maria','salino','00020152',365)

user1.greet_user()
user2.greet_user()
user3.greet_user()
