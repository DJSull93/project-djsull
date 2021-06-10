import os
os.environ.setdefault("DJANGO_SETTING_MODULE", "django_prj.settings")
from crime_cctv.services import CrimecctvService


class CrimeAPI(object):

    @staticmethod
    def main():
        crimeService = CrimecctvService()
        while 1:
            m = input('1. print csv, 2. , 3. , 4. , 5. print xlsx')
            if m == '0':
                break
            elif m == '1':
                crimeService.csv({'context':'./data/', 'fname':'cctv_in_seoul'})
            elif m == '2':
                crimeService.csv({'context': './data/', 'fname': 'crime_in_seoul'})
            elif m == '3':
                crimeService.csv({'context': './data/', 'fname': 'police_position'})
            elif m == '4':
                crimeService.csv({'context': './data/', 'fname': 'us_unemployment'})
            elif m == '5':
                crimeService.xls({'context': './data/', 'fname': 'pop_in_seoul'})
            else:
                continue

CrimeAPI.main()