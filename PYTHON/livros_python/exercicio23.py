""" 
9.6 Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma classe
chamada IceCreamStand que herde da classe Restaurant do Exercício 9.1 (página 208)
ou Exercício 9.4 (página 214). Qualquer uma das versões da classe funcionará; basta
escolher a que você mais gosta. Adicione um atributo chamado flavors que armazene
uma lista de sabores de sorvete. Escreva um método que exiba esses sabores. Crie
uma instância a partir de IceCreamStande chame esse método.

9.7 Admin: Um administrador é um tipo especial de usuário. Crie uma classe chamada
Admin que herde da classe User escrita no Exercício 9.3 (página 209) ou Exercício 9.5
(página 214). Adicione um atributo, privileges, que armazene uma lista de strings como
"can add post", "can delete post", "can ban user", e assim por diante. Escreva um
método chamado show_privileges() que enumere o conjunto de privilégios do
administrador. Crie uma instância Admin e chame seu método.

9.8 Privilégios: Crie uma classe Privileges separada. A classe deve ter um atributo,
privileges, que armazene uma lista de strings, conforme descrito no Exercício 9.7.
Passe o método show_privileges() para essa classe. Crie uma instância de Privileges
como um atributo na classe Admin. Crie uma instância nova de Admin e use seu
método para mostrar seus privilégios.


"""

from exercicio21 import Restaurant,User



class IceCreamStand(Restaurant):
    """ Sorveteria."""
    
    def __init__(self, restaurant_name, cuisine_type,):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Orange', 'Chocolate','Strawberry','Mint Chocolate Chip','Caramel ']


    def describe_flavors(self):
        for flavor in self.flavors:
            print(f'- {flavor}')
            



class Admin(User):

    
    def __init__(self,first_name,last_name,documento, idade):
        super().__init__(first_name,last_name, documento, idade)
        self.privileges = Privileges() 
    
    




class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        for privilege in enumerate(self.privileges):
            print(f'{privilege[0]} : {privilege[1]}')    
sorveteria1 = IceCreamStand('Açai Leão', 'sorveteria')            
sorveteria1.describe_flavors()

adm = Admin('matheus','santos','00028922',24)
adm.show_privileges()