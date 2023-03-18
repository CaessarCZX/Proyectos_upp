"""
Tenemos la clase dispositivo

con tres hijas de:
celular
tablet
speaker


"""
class device():
    def __init__(self, provider, year):
        self.__provider = provider
        self.__year = year

    def type_of_device(self):
        return f"The type of device is {type(self).__name__}"
    
    def get_provider(self):
        return self.__provider
    
    def get_year(self):
        return self.__year
    
class phone(device):
    model = 'ULTIMATE'

    def __init__(self, provider, year):
        super().__init__(provider, year)

    def description(self):
        return f"The phone is provided for {self.get_provider()} and was manufactured in {self.get_year()} and is a model {self.model}"
    
class tablet(device):
    model = 'G85'

    def __init__(self, provider, year):
        super().__init__(provider, year)

    def description(self):
        return f"The tablet is provided for {self.get_provider()} and was manufactured in {self.get_year()} and is a model {self.model}"

class speaker(device):
    model = 'SUPERBASS' 

    def __init__(self, provider, year):
        super().__init__(provider, year)

    def description(self):
        return f"The speaker is provided for {self.get_provider()} and was manufactured in {self.get_year()} and is a model {self.model} "
    

if __name__ == '__main__':
    nokia = phone('china', 2023)
    print(nokia.description())
    print(nokia.type_of_device()+'\n')
    ipad = tablet('taiwan', 2022)
    print(ipad.description())
    print(ipad.type_of_device()+'\n')
    lgboom = speaker('singapore', 2011)
    print(lgboom.description())
    print(lgboom.type_of_device()+'\n')
    