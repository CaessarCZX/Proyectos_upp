"""
Clase: Contacto telefonico
Atributos privados: Numero de telefono, Nombre
"""

import re

class Contact:   
    def __init__(self, number, name):
        self.__number = number
        self.__name = name
    
    @property
    def number(self):
        return self.__number
    
    @property
    def name(self):
        return self.__name
    
    @number.setter
    def number(self, newNumber):        
        if len(newNumber) == 10 and re.match("^[0-9]*$", newNumber):
            self.__number = newNumber
            print(f"El numero de telefono es: {self.__number}")
        else:
            print("Es incorrecto este numero de telefono")
    
    @name.setter
    def name(self, newName):
        try:
            newName= str(newName)
        except:
            newName = "NoValid"
        
        if (newName != "" or newName != "NoValid"):
            self.__name = newName
            print(f"Este telefono le pertenece a {self.__name}")
        else:
            print("Este es un nombre no valido")

if __name__ == "__main__":
    contact_1 = Contact("9994379885", "Axel")
    contact_1.number = "9993574151"
    contact_1.name = "Axel"