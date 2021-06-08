from crime_cctv.models import CrimeDTO
from crime_cctv.services import CrimecctvService
from common.services import CommonService

class CrimeAPI(object):

    @staticmethod
    def main():
        util = CrimecctvService()
        dto = CrimeDTO()
        serv = CommonService()
        while 1:
            m = input('1. print csv, 2. print xlsx')
            if m == '0':
                break
            elif m == '1':
                dto.dframe = util.new_model_csv('cctv_in_seoul.csv')
                serv.print_dframe(dto.dframe)
            elif m == '2':
                dto.dframe = util.new_model_xlsx('pop_in_seoul.xls')
                serv.print_dframe(dto.dframe)
            else:
                continue

CrimeAPI.main()