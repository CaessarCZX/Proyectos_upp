"""
Vamos a crear una clase llamada cafe la cual sera la clase a heredar

Las 3 clases a heredar son:
-Mochiatto
-Espresso
-Americano
"""

class coffee():
    def __init__(self, origin_country, temperature):
        self.__origin_country = origin_country
        self.__temperature = temperature

    def type_of_coffe(self):
        return f'The type of coffe is {type(self).__name__}'
    
    def get_origin_country(self):
        return self.__origin_country
    
    def get_temperature(self):
        return self.__temperature

class mocchiatto(coffee):
    price = 25.5

    def __init__(self, origin_country, temperature):
        super().__init__(origin_country, temperature)

    def description(self):
        return f'This coffee is originary from {self.get_origin_country()} its ideal temperature is {self.get_temperature()} and its cost is ${self.price}'
    
class espresso(coffee):
    price = 30.0
    def __init__(self, origin_country, temperature):
        super().__init__(origin_country, temperature)

    def description(self):
        return f'This coffee is originary from {self.get_origin_country()} its ideal temperature is {self.get_temperature()} and its cost is ${self.price}'

class american(coffee):
    price = 20.5

    def __init__(self, origin_country, temperature):
        super().__init__(origin_country, temperature)

    def description(self):
        return f'This coffee is originary from {self.get_origin_country()} its ideal temperature is {self.get_temperature()} and its cost is ${self.price}'
        
if __name__ == '__main__':
    coffee1 = mocchiatto('Italy', '120 F')
    print(coffee1.type_of_coffe())
    print(coffee1.description() + '\n')
    coffee2 = espresso('Colombia', '140 F')
    print(coffee2.type_of_coffe())
    print(coffee2.description() + '\n')
    coffee3 = american('Hawaii', '120 F')
    print(coffee3.type_of_coffe())
    print(coffee3.description() + '\n')
