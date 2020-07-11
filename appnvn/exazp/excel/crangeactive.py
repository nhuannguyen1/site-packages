from pynvn.excel.copypasteexell import cprange
import xlwings as xw
from pynvn.csv.rcsv import returndictrowforcsv
from pynvn.string.slist import returnseplistintbbystr
class crangeactive:
    """ copy sheet and change value cell """
    def __init__(self,pathconf = None,
                pathconfigexcelcopy = None):
        # call dict 
        self.pathconfigexcelcopy = pathconfigexcelcopy
        dictconf = returndictrowforcsv(path=pathconf)
        self.__hm_startcopyrange = dictconf["hm_startcopyrange"]
        self.__startcopyrange = returnseplistintbbystr(self.__hm_startcopyrange)
        self.__hm_startpasterange = dictconf["hm_startpasterange"]
        self.__hm_hangmuc = dictconf["hm_hangmuc"]
        self.__copyrangfromconf()
    def __copyrangfromconf(self):        
        sheetdesactive = xw.sheets.active
        start,end = self.__startcopyrange
        
        cprange(pathtocopy=self.pathconfigexcelcopy,
                pathtodes=sheetdesactive,
                rangetocopy=self.__hm_startcopyrange,
                rangetopaste=self.__hm_startpasterange)
        sheetdesactive.range("{0}{1}:{0}{2}".format(self.__hm_hangmuc,start + 2,end)).value  = sheetdesactive.name