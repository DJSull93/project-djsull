from crime_cctv.models import CrimeDTO
import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

class CrimecctvService(object):

    dto = CrimeDTO()

    def new_model_csv(self, payload):
        this = self.dto
        this.context = './data/'
        this.fname = payload
        df_csv = pd.read_csv(this.context + this.fname)
        return df_csv

    def new_model_xlsx(self, payload):
        this = self.dto
        this.context = './data/'
        this.fname = payload
        #sheet = xw.Book(this.context + payload + '.xls')
        df_xlsx = pd.read_excel(this.context + this.fname)
        return df_xlsx