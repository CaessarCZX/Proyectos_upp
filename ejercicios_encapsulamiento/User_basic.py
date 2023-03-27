'''
Vamos a crear la claser ususario con los sigueinetes atributos
>>> nombre(verificacion), password(verificacion), edad(verificacion)
obtendremos los atributos a traves de los getters y setters 
@property
@attrib.setter
'''
import re

class Basic_user():
    def __init__(self, name, age, password = '00000000'):
        self.__name = name
        self.__password = password
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @property
    def password(self):
        return self.__password
    
    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self, name):
        aproved_len = 3
        
        if len(name) > aproved_len:
            print('Nombre valido')
        else:
            print('Nombre demasiado corto, no valido')

    #Esta funcion verifica que el password a ingresar contenga al menos un caracter en: mayuscula, minuscula, numero y
    # simbolo especial, al igual de que el pasword sea de al menos 8 caracteres.    
    @password.setter
    def password(self, password):
        if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
            self.__password = password
            print('Password aceptado')
        else:
            print('Password denegado')
            
        
    @age.setter
    def age(self, age):
        min_age = 18

        try:
            age = int(age)
        except:
            age = 7

        if age < min_age:
            print('No tiene suficiente edad para acceder')
        else:
            self.__age = age
            print('Edad correcta')

    def user_details(self):
        return f'The user name is: {self.name}, age: {self.age} and the password user is: {self.password}'
        
if __name__ == '__main__':
    usuario_nuevo = Basic_user('Carlos Gonzales', 25)
    usuario_nuevo.age = 26
    usuario_nuevo.password = 'MyPassword123$'
    print(usuario_nuevo.user_details())
    
