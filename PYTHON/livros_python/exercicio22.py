from exercicio20 import Car

""" 
9.9 Trocar bateria: Utilize a versão final do electric_car.py dessa seção. Adicione um
método à classe Battery chamado upgrade_battery(). Esse método deve verificar o
tamanho da bateria e definir a capacidade como 65, caso necessário. Crie um carro
elétrico com um tamanho default de bateria, chame get_range() uma vez e, depois,
chame get_range() uma segunda vez, após atualizar a bateria. Você deve ver aumento
no alcance de distância do carro.

"""

class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""
    def __init__(self, battery_size=40):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size


    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    

    def get_range(self):
        """Exibe frase sobre a distância que o carro percorre com essa bateria"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")        
        

    def upgrade_battery(self):        
        self.battery_size = 65
        
        
class ElectricCar(Car):

    """Representa aspectos de um carro, específicos para veículos elétricos"""
    def __init__(self,make, model, year):
        super() .__init__(make, model, year)
        self.battery = Battery()



    def fill_gas_tank(self):
        """Carros elétricos não têm tanques de gasolina"""
        print("This car doesn't have a gas tank!")
        
        
        
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
