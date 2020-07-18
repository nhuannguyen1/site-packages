from pynvn.excel.copypasteexell import cprange
import xlwings as xw
from pynvn.csv.rcsv import returndictrowforcsv
from pynvn.string.slist import returnseplistintbbystr
from pynvn.excel import activesheet
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
        # copy another range botton
        self.__hm_startcopyrangebt = dictconf["hm_startcopyrange_bt"]
        self.__startcopyrangebt = returnseplistintbbystr(self.__hm_startcopyrangebt)
        self.__hm_startpasterangebt = dictconf["hm_startpasterange_bt"]
        
        self.__sheetdesactive = activesheet()
        
        self.copyrangfromconf()
        #self.__copyrangfromconf_bt()
    def copyrangfromconf(self):        
        start,end = self.__startcopyrange
        cprange(pathtocopy=self.pathconfigexcelcopy,
                pathtodes=self.__sheetdesactive,
                rangetocopy=self.__hm_startcopyrange,
                rangetopaste=self.__hm_startpasterange)
        self.__sheetdesactive.range("{0}{1}:{0}{2}".format(self.__hm_hangmuc,start + 2,end)).value  = self.__sheetdesactive.name
    def copyrangfromconf_bt(self):        
        cprange(pathtocopy=self.pathconfigexcelcopy,
                pathtodes=self.__sheetdesactive,
                rangetocopy=self.__hm_startcopyrangebt,
                rangetopaste=self.__hm_startpasterangebt)
