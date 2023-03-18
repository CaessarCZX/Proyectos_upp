"""
Vamos a crear un clase operador movil que nos servira como principal

De la clase anterior heredaremos estas 3 clases:
-Telcel
-At&t
-Movistar
"""

class mobile_operator():
    def __init__(self, ceo, origin_country):
        self.__ceo =ceo
        self.__origin_country = origin_country

    def type_of_operator(self):
        return f'The type of operator is {type(self).__name__}'
    
    def get_ceo(self):
        return self.__ceo
    
    def get_origin_country(self):
        return self.__origin_country
    
class telcel(mobile_operator):
    starting_price = 10.0

    def __init__(self, ceo, origin_country):
        super().__init__(ceo, origin_country)

    def description(self):
        return f'The mobile operator CEO is {self.get_ceo()} its origin country is {self.get_origin_country()} and its starting plan cost ${self.starting_price}'

class atyt(mobile_operator):
    starting_price = 10.0

    def __init__(self, ceo, origin_country):
        super().__init__(ceo, origin_country)

    def description(self):
        return f'The mobile operator CEO is {self.get_ceo()} its origin country is {self.get_origin_country()} and its starting plan cost ${self.starting_price}'

class movistar(mobile_operator):
    starting_price = 15.0

    def __init__(self, ceo, origin_country):
        super().__init__(ceo, origin_country)

    def description(self):
        return f'The mobile operator CEO is {self.get_ceo()} its origin country is {self.get_origin_country()} and its starting plan cost ${self.starting_price}'

if __name__ == '__main__':
    operator_1 = telcel('Danie Aboumrad', 'Mexico')
    print(operator_1.type_of_operator())
    print(operator_1.description() + '\n')
    operator_2 = atyt('John Stankey', 'USA')
    print(operator_2.type_of_operator())
    print(operator_2.description() + '\n')
    operator_3 = movistar('Sergio Olse', 'Spain')
    print(operator_3.type_of_operator())
    print(operator_3.description() + '\n')