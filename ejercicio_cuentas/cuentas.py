"""
1.  Crear "cuentas" bancaria.
2.  Para poder crear una 
    cuentass es necesario pasarle su respectivo usuario.
3.  El balance inicial de apertura es opcional
4.  Crear metodos retirar() y deposito () de los atributos 
    solo seran modificables a traves de los setters.
5.  Crear un metodo mostrar_datos() que muestre 
el nombre de usuario y el balance total.

"""
from usuarios import usuarios 

class cuentas():
    def __init__(self, usuario: usuarios , balance = 0.0):
        self.__usuario = usuario
        self.__balance =  balance
    
    def retirar(self, monto):
        if self.validar_retiro(monto):
            self.__balance -= monto
        else:
            print('No hay dinero suficiente')

    def depositar(self, monto):
        self.__balance += monto

    def validar_retiro(self, monto):
        # Validar suficiente saldo
        if monto <= self.__balance:
            return True
        
    def get_balance(self):
        return self.__balance

    def get_usuario(self):
        return self.__usuario.get_nombre()
    
    def get_edad(self):
        return self.__usuario.get_edad()

    def mostrar_datos(self):
        return f"Nombre de usuario: {self.get_usuario()}\nBalance total: {self.get_balance()}$"    

"""
if __name__ == '__main__':
    usuario = usuarios('Carlos', 25, 'hhhhhhhhhhhhhhhhhh')
    cuentas = cuentas(usuario, 100)
    cuentas.retirar(1500)
    # print(cuentas.mostrar_datos())
    print(cuentas.validar_retiro())

"""