from common.models import FileDTO
from common.services import Printer, Reader
from common.abstracts import ReaderBase


class CrimecctvService(ReaderBase):

    def csv(self, payload):
        file = FileDTO()
        printer = Printer()
        reader = Reader()
        file.context = payload.get('context')
        file.fname = payload.get('fname')
        printer.dframe(reader.csv(file))

    def xls(self, payload):
        file = FileDTO()
        printer = Printer()
        reader = Reader()
        file.context = payload.get('context')
        file.fname = payload.get('fname')
        printer.dframe(reader.xls(file, header=1, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

    def json(self, payload):
        pass

    def new_file(self):
        pass