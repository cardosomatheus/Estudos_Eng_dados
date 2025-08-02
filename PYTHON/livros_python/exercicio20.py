class Car:
    """Simples tentativa de representar um carro"""
    def __init__(self, make, model, year):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
        
    def get_descriptive_name(self):
        """Retorna um nome descritivo, formatado elegantemente"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro, em milhas"""
        print(f"This car has {self.odometer_reading} miles on it.")

    
    def update_odometer(self,mileage): 
        """Define a leitura do hodômetro para o valor fornecido"""
         
        if  mileage >=  self.odometer_reading:
            self.odometer_reading = mileage        
        else:
            print("You can't roll back an odometer!")


    def increament_odometer(self , miles):
        """Adiciona a quantidade fornecida à leitura do hodômetro"""        
        self.odometer_reading += miles            


    def fill_gas_tank(self):
        """Carros elétricos não têm tanques de gasolina"""
        print("GAAAAAAAAAAAAAAAAAAAAAAAAAS!")        
 
 
 
        
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(1000)
my_new_car.update_odometer(30)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()