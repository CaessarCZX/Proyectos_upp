'''
Clase:FABRICANTE DE LAPTO CHINO
Atributos: processor, ssd, sed_code
getter: @property
setter: @fucntion.setter

'''

class chinese_factory():
    def __init__(self, processor = '', ssd = 0):
        self.__processor = processor
        self.__ssd = ssd

    @property
    def processor(self):
        return self.__processor
    
    @property
    def ssd(self):
        return self.__ssd
    
    @ssd.setter
    def ssd(self, new_ssd):
        max_memory = 4
        min_memory = 1

        try:
            new_ssd = int(new_ssd)
        except:
            new_ssd = 0

        if new_ssd <= max_memory or new_ssd >= min_memory:
            self.__ssd = new_ssd
            print('La memoria tiene una unidad vallida')
        else:
            print('Unidad de memoria invalida')
    
    @processor.setter
    def processor(self, new_processor):
        num_char = 9

        if len(new_processor) > num_char:
            self.__processor = new_processor
            print('Cambio valido')
        else:
            print('Cambio no valido')

    def specs(self):
        return f'This factory has available the processor {self.processor} and memories of {self.ssd}'

if __name__ == '__main__':
    fabrica = chinese_factory()
    fabrica.processor = 'DSDJFSKJFLSJSDC'
    fabrica.ssd = 4
    print(fabrica.specs())
