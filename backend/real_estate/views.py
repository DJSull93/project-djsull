import pandas as pd
from real_estate.models import HousingDTO
from real_estate.services import HousingService

class HousingAPI(object):

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. exel type is {type(this.KBhousing)}')
        print(f'2. exel colums is \n{this.KBhousing.columns}')
        print(f'3. exel TOP is \n{this.KBhousing.head()}')
        print(f'4. exel number of null is \n{this.KBhousing.isnull().sum()}')

    @staticmethod
    def main():
        util = HousingService()
        dto = HousingDTO()
        while 1:
            m = input('0. EXIT 1. make model 2. make Dataframe ')
            if m == '0':
                break
            elif m == '1':
                dto.dframe = util.new_model('housing')
                HousingAPI.print_this(dto.dframe)
            elif m == '2':
                util.remove_none_in_gugun(dto.dframe)
            else:
                continue

Controller.main()
'''
if __name__ == '__main__':
    c = Controller()
    c.preprocess('KBhousing.xlsx')
'''