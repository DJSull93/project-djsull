class Country(object): # super class
    name = 'Country Name'
    population = 'Population'
    capital = 'Capital'

    def show(self):
        print('Country Class Method')


class Korea(Country): # sub class

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'Country Name is {self.name}')


def execute():
    k = Korea("KOREA")
    k.show_name()


execute()