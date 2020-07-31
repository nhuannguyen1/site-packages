from pynvn.excel import col2num,colnum_string, repathlinkexcel
from pynvn.csv.todict import returndictrowforcsv
from pynvn.excel.fomulas import vlookup 
from pynvn.excel import sheet_by_namesheet
import xlwings as xw
class fformulas:
    """ fill the formulas into excel file """
    def __init__(self, retr_path = None,
                        retr_sheetname =None, 
                        des_path = None,
                        des_sheetname =None,
                        fuction = None,
                        pathconf = None,
                        ):
        self.dictconf = returndictrowforcsv(path=pathconf)
        self.__retr_path = retr_path
        self.__retr_sheetname = retr_sheetname
        self.__des_path = des_path
        self.__des_sheetname = des_sheetname
        self.__fuction = fuction
        self.__pexcelretr = repathlinkexcel(usingfullname=True,
                                            fullname=retr_path,
                                            namefile=retr_sheetname,
                                            namesheet=self.__retr_sheetname
                                            )
        self.ws_des = sheet_by_namesheet(path=des_path,namesheet=des_sheetname)
    def filltoexcell(self):
        if self.__fuction == "VLOOKUP":
            vlvalue = self.dictconf["Sub_VLOOKUP_Lookup_value"]
            vTaalue = self.dictconf["Sub_VLOOKUP_table_array"]
            vrlalue = self.dictconf["Sub_VLOOKUP_range_lookup"]
            clgvalue = self.dictconf["Sub_VLOOKUP_Column_Get_Value"]
            clrvvalue = self.dictconf["Sub_VLOOKUP_Locc_result_value"]
            
            valuetest = vlookup(loopkup_value_range=vlvalue,
                                table_array=vTaalue,
                                plexcel=self.__pexcelretr,
                                colum_to_get_value = clgvalue,
                                ws_des = self.ws_des,
                                Sub_VLOOKUP_Locc_result_value= clrvvalue
                                ).forexelldes()


        



 
                                                                                        