"""
1. Crear una clase usuario 
2. Attrib: nombre, edad, curp
3. validaar que el curp sea == 18
4. Definir un metodo que muestre los datos del usuario (Todos los atributos)
5. Definir un metodo que muestre si la edad del ususario es mayor o igual a 18
"""
class usuarios():
    def __init__(self, nombre, edad, curp):
        self.__nombre = nombre 
        if self.validate_edad(edad) == None:
            return "Edad invalida"
        self.__edad = edad
        if self.validate_curp(curp) == None:
            return 'CURP invalido'
        self.__curp = curp

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_curp (self):
        return self.__curp

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        if self.validate_edad(edad):
            self.__edad = edad
        else:
            print('Edad invalida')

    def set_curp(self, curp):
        if self.validate_curp(curp):
            self.__curp = curp

    def validate_curp(self, curp):
        if len(curp) == 18:
            return curp

    def get_all_attribute(self):
        return f"Nombre de usuario: {self.__nombre}\nEdad de ususario: {self.__edad}\nCurp: {self.__curp}"
    
    def validate_edad(self, edad):
        if edad >= 18:
            return edad

'''
if __name__ == '__main__': 
    usuario1 = usuarios('Carlitos', 18, 'gggggggggggggggggg')
    print(usuario1.get_all_attribute())
    usuario1.set_edad(29)
    print(usuario1.get_all_attribute())
'''    

