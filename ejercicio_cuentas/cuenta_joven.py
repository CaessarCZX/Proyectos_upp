"""
1. Crear clase cuenta_joven.
2. Heredan de clase "cuentas" pero obtienen una bonificacion por abrir la cuenta.
3. Titular debe ser de un rango de edad de entre 18 y 25 anos de edad (Usar verificacion). NOTA - La verificacion se hara por fuera de objeto.
4. Un usuario de esta clase de cuenta cambiara a cuenta regular despues de los 25 (Hacer upgrade de cuenta automatico). NOTA - SEl upgrade se hara por fuera del objeto.
5. Sus datos deben poder ser mostrados explicitamente con el tipo de cuenta y adjuntar la bonificacion que se les otorgo.
"""

from usuarios import usuarios
from cuentas import cuentas

class cuentas_joven(cuentas):
    def __init__(self, usuario: usuarios, balance=0, bonificacion = 0.05):
        super().__init__(usuario, balance)
        self.__bonificacion = bonificacion
        self.__status_bonificacion = False
        if super().get_balance() != 0:
            self.add_bonificacion()

    def add_bonificacion(self):
        self.__bonificacion *= super().get_balance()

        if self.__status_bonificacion == False:
            super().depositar(self.__bonificacion)
            return True

    def mostrar_datos(self):
        return f"Cuenta Joven.\n"+super().mostrar_datos()+f"\nCon bonificacion de: {self.__bonificacion}$"
    
        