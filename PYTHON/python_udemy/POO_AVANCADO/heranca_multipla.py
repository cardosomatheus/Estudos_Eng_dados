# Herança multipla 

class Animal:
    
    @property
    def capacidades(self):
        return ('andar','comer','beber')
    

class Homem(Animal):

    @property
    def capacidades(self):
        return super().capacidades+('amar','falar','jogar truco')
    


class Aranha(Animal):

    @property
    def capacidades(self):
        return super().capacidades+('soltar teia','andar pela parede')

class HomemAranha(Homem,Aranha):

    @property
    def capacidades(self):
        return super().capacidades + ('bater em bandido', 'pular em predios')
    


rato = Animal()
jorge = Homem()
dona_aranha = Aranha()
petter = HomemAranha()

print('animal: ',rato.capacidades)
print('Homen: ',jorge.capacidades)
print('Aranha: ',dona_aranha.capacidades)
print('Homen aranha: ',petter.capacidades)