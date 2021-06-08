class CommonService(object):

    def print_dframe(self, this):
        print('*' * 100)
        print(f'1. target type is {type(this)}')
        print(f'2. target colums is \n{this.columns}')
        print(f'3. target TOP is \n{this.head()}')
        print(f'4. target number of null is \n{this.isnull().sum()}')
        print('*' * 100)