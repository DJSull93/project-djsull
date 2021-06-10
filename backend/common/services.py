import pandas as pd
import json
from common.abstracts import PrinterBase, ReaderBase
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


class Printer(PrinterBase):

    def dframe(self, this):
        print('*' * 100)
        print(f'1. target type is {type(this)}')
        print(f'2. target colums is \n{this.columns}')
        print(f'3. target TOP is \n{this.head()}')
        print(f'4. target number of null is \n{this.isnull().sum()}')
        print('*' * 100)


class Reader(ReaderBase):

    def new_file(self, file) -> str:
        return file.context + file.fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',')

    def xls(self, file, header, usecols) -> object:
        return pd.read_excel(f'{self.new_file(file)}.xls', header=header, usecols=usecols)

    def json(self, file) -> object:
        return json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))
