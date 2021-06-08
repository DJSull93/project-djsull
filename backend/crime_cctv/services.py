from crime_cctv.models import CrimeDTO
import pandas as pd
import xlwings as xw

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