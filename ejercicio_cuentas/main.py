from usuarios import usuarios
from cuentas import cuentas
from cuenta_joven import cuentas_joven



if __name__ == '__main__':
    usuario = usuarios('Raul', 18, 'hhhhhhhhhhhhhhhhhh')
    cuenta = cuentas_joven(usuario)
    print(cuenta.mostrar_datos())
    cuenta.depositar(1000)
    print(cuenta.mostrar_datos())
    cuenta.add_bonificacion()
    print(cuenta.mostrar_datos())