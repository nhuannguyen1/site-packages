from pynvn.excel.list import pairslistfromexcel,removevalueinlistpair
from pynvn.csv.tocsv import pairlistinlisttocsv
import xlwings as xw
class hconfazb:
    def __init__(self,pathconf,pathexconf):
        self.pathconf = pathconf
        self.__app = xw.App(visible=False)
        self.__wb_excel= xw.Book(pathexconf)
        ws_excels =self.__wb_excel.sheets
        self.__ws_excel = ws_excels["hrdata_modified"]
    def convertocsv(self):
        """convert to csv """
        # createv pair list form excel 
        listepairsremoved = removevalueinlistpair(lista=pairslistfromexcel(sheet=self.__ws_excel))
        # to csv
        pairlistinlisttocsv(listvalue=listepairsremoved,
                                        pathcsv=self.pathconf)
        self.__wb_excel.close()
        self.__app.quit()
