"""
Vamos a crear la clase compania que sera del que hereden la demas clases

craremos 3 clases herederas
-Tesla
-Roku
-Apple
"""

class company():
    def __init__(self, foundation_comp, founder):
        self.__foundation_comp = foundation_comp
        self.__founder = founder

    def type_of_company(self):
        return f'The type of company is {type(self).__name__}'
    
    def get_foundation_comp(self):
        return self.__foundation_comp
    
    def get_founder(self):
        return self.__founder
    
class tesla(company):
    product_star = 'Model 3'

    def __init__(self, foundation_comp, founder):
        super().__init__(foundation_comp, founder)

    def description(self):
        return f'The company was founded in the year {self.get_foundation_comp()} and its founder is {self.get_founder()}, the company star product is {self.product_star}'

class roku(company):
    product_star = 'Stick 4k'

    def __init__(self, foundation_comp, founder):
        super().__init__(foundation_comp, founder)

    def description(self):
        return f'The company was founded in the year {self.get_foundation_comp()} and its founder is {self.get_founder()}, the company star product is {self.product_star}'

class apple(company):
    product_star = 'iphone'

    def __init__(self, foundation_comp, founder):
        super().__init__(foundation_comp, founder)

    def description(self):
        return f'The company was founded in the year {self.get_foundation_comp()} and its founder is {self.get_founder()}, the company star product is {self.product_star}'

if __name__ == '__main__':
    company_one = tesla(2003, 'Elon Musk')
    print(company_one.type_of_company())
    print(company_one.description() + '\n')
    company_two = roku(2002, 'Anthony Wood')
    print(company_two.type_of_company())
    print(company_two.description() + '\n')
    company_three = apple(1976, 'Steve Jobs')
    print(company_three.type_of_company())
    print(company_three.description() + '\n')
