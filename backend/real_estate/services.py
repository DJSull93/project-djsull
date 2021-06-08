from real_estate.models import HousingDTO
import pandas as pd
import xlwings as xw
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

class HousingService(object):

    dto = HousingDTO()

    # DF 생성하기
    def new_model(self, payload) -> object:
        this = self.dto
        this.context = './data/'
        this.fname = payload
        sheet = xw.Book(this.context + payload + '.xlsx').sheets['매매종합']
        row_num = sheet.range(1, 1).end('down').end('down').end('down').row
        data_range = 'A2:g2' + str(row_num)
        df = sheet[data_range].options(pd.DataFrame, index=False, header=True).value
        return df

    # 시 도 데이터 리스트 만들기

    #