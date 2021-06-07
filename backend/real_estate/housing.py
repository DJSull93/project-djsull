from real_estate.dataset import Dataset
import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

class Housing(object):

    dataset = Dataset()

    # DF 생성하기
    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname, sheet_name='평균전세')

    # 시 도 데이터 리스트 만들기

    #