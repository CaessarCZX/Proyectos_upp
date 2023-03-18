"""
Vamos a crear un clase principal que se llamara dragon de la que heredaran las demas

Las 3 clases que heredaran son:
-dragon fuego
-dragon agua
-dragon tierra
"""

class dragon():
    def __init__(self, resistance, hp):
        self.__resistance = resistance
        self.__hp = hp

    def type_of_dragon(self):
        return f'The type of dragon invoked is {type(self).__name__}'
    
    def get_resistance(self):
        return self.__resistance
    
    def get_hp(self):
        return self.__hp
    
class d_fire(dragon):
    special_power = 'Huge llamarada'

    def __init__(self, resistance, hp):
        super().__init__(resistance, hp)

    def description(self):
        return f'Our dragon have a resistance of {self.get_resistance()} it have a {self.get_hp()} of HP and its special power is {self.special_power}'

class d_water(dragon):
    special_power = 'Aqua Pulse'

    def __init__(self, resistance, hp):
        super().__init__(resistance, hp)

    def description(self):
        return f'Our dragon have a resistance of {self.get_resistance()} it have a {self.get_hp()} of HP and its special power is {self.special_power}'

class d_earth(dragon):
    special_power = 'Abyss Terremote'

    def __init__(self, resistance, hp):
        super().__init__(resistance, hp)

    def description(self):
        return f'Our dragon have a resistance of {self.get_resistance()} it have a {self.get_hp()} of HP and its special power is {self.special_power}'

if __name__ == '__main__':
    dragon1 = d_fire(750, 850)
    print(dragon1.type_of_dragon())
    print(dragon1.description() + '\n')
    dragon2 = d_water(625, 900)
    print(dragon2.type_of_dragon())
    print(dragon2.description() + '\n')
    dragon3 = d_earth(1000, 750)
    print(dragon3.type_of_dragon())
    print(dragon3.description() + '\n')