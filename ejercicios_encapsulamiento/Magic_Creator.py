"""
Clase: Mago
Atributos privados: poder elementar, nivel de magia
"""
class Magician:   
    def __init__(self, elementalPower = "", magicLevel = 0):
        self.__elementalPower = elementalPower
        self.__magicLevel = magicLevel
    
    @property
    def elementalPower(self):
        return self.__elementalPower
    
    @property
    def magicLevel(self):
        return self.__magicLevel
    
    @elementalPower.setter
    def elementalPower(self, newElementalPower):
        try:
            newElementalPower = str(newElementalPower)
        except:
            newElementalPower = "No valido"
        
        if newElementalPower == "Fuego" or newElementalPower == "Electrico":
            self.__elementalPower = newElementalPower
            print(f"Uso mi poder de {self.__elementalPower}")
        else:
            print("Este no es un poder magico")
    
    @magicLevel.setter
    def magicLevel(self, newMagicLevel):
        try:
            newMagicLevel = int(newMagicLevel)
        except:
            newMagicLevel = 1
        
        if (newMagicLevel >= 1 and newMagicLevel <= 100):
            self.__magicLevel = newMagicLevel
            print(f"He subido al nivel: {self.__magicLevel}")
        else:
            print("Hubo un problema al subir de nivel")

if __name__ == "__main__":
    magician_1 = Magician("Electrico", 25)
    magician_1.elementalPower = "Fuego"
    magician_1.magicLevel = 30