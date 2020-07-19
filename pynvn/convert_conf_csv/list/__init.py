from pynvn.excel.copypasteexell import cprange
import xlwings as xw
from pynvn.csv.rcsv import returndictrowforcsv
from pynvn.string.slist import returnseplistintbbystr
from pynvn.excel import activesheet,activeworkbook
from pynvn.csv.tolist import convertcsvto1list
from pynvn.path.ppath import refullpath,getdirpath
def conf_csvtolist (pathconf,path_csvtoconverttolist)
    """ copy sheet and change value cell """
    # call dict 
    dictconf = returndictrowforcsv(path=pathconf)
    # return csv have list sheet name 
    self.pathlsn = refullpath(dirpath=self.dirpathconf,
                                        filename=listsheetnamehm)
    copyhm = dictconf["copyhm"]
    try:                        
        self.lsheetname = convertcsvto1list(path=path_csvtoconverttolist)
    except:
        pass
