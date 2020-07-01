from pynvn.excel import col2num
from pynvn.string.slist import returnseplistintbbystr,str_seplistintbbystr
from xlwings as xw
class azb10:
    """copy excel to excel"""
    def __init__(self,
                    dictconf = None,
                    wsheetdes = None,
                    mrowwscopy = None,
                    mcolumnwscopy = None,
                    wsheetcopy = None
                ):
        self.__wsheetcopy = wsheetcopy
        self.__mrowwscopy = mrowwscopy
        self.__mcolumnwscopy = mcolumnwscopy
        self.__wsheetdes = wsheetdes
        self.__azb10startr = int(dictconf["azb10startr"])
        #line azb10s folow row at mother
        self.__zab10_recor_l1m = int(dictconf["zab10_recor_l1m"])
        self.__zab10_recor_l2m = int(dictconf["zab10_recor_l2m"])
        self.__zab10_recor_l3m = int(dictconf["zab10_recor_l3m"])
        # azb10 for both
        self.__zab10_totalpaodstr = (dictconf["zab10_totalpaod"])
        self.__zab10_totalpaod = col2num(dictconf["zab10_totalpaod"])
        self.__zab10_frmpstr = (dictconf["zab10_frmp"])
        self.__zab10_frmp = col2num(dictconf["zab10_frmp"])
        self.__zab10_refundstr = (dictconf["zab10_refund"])
        self.__zab10_refund = col2num(dictconf["zab10_refund"])
        self.__zab10_efastr = (dictconf["zab10_efa"])
        self.__zab10_efa = col2num(dictconf["zab10_efa"])
        self.__zab10_finalabstr = (dictconf["zab10_finalab"])
        self.__zab10_finalab = col2num(dictconf["zab10_finalab"])
        self.__zab10_nbstr = (dictconf["zab10_nb"])
        self.__azb10_ms = col2num(dictconf["azb10_ms"])
        self.__zab10_nb = col2num(dictconf["zab10_nb"])
        self.__listsubtal = [self.__zab10_totalpaod,
                            self.__zab10_frmp,
                            self.__zab10_refund,
                            self.__zab10_efa,
                            self.__zab10_finalab,
                            self.__zab10_nb]
        self.__listsubtalstr = [self.__zab10_totalpaodstr,
                            self.__zab10_frmpstr,
                            self.__zab10_refundstr,
                            self.__zab10_efastr,
                            self.__zab10_finalabstr,
                            self.__zab10_nbstr]
        self.__indexvaluerc = [self.__zab10_recor_l1m,
                            self.__zab10_recor_l2m,
                            self.__zab10_recor_l3m]

        self.__azb10netbi =col2num (dictconf["azb10netbi"])
        self.__listmaxrc = self.__indexvaluerc + [self.__mrowwscopy]
    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """
        l,m = 0,0
        for i in range (self.__azb10startr, self.__mrowwscopy):
            valuee = self.__wsheetcopy.range(i,self.__azb10_ms).value
            # value of Resource Code/Mã Tài nguyên
            valuerc = self.__wsheetcopy.range(i,2).value
            if valuerc != None:
                m = self.__indexvaluerc[l]
                l = l + 1
            if valuee != None:
                for j in range (1, self.__mcolumnwscopy + 1):
                    if (j in self.__listsubtal) and (valuerc != None):

                        self.__wsheetdes.range(m,j).value = '=SUBTOTAL(9,{2}{0}:{2}{1})'.format(m + 1,
                                                                                    self.__listmaxrc[l] - 1,
                                                                                    self.__listsubtalstr[self.__listsubtal.index(j)])
                    else:
                        self.__wsheetdes.range(m,j).value = self.__wsheetcopy.range(i,j).value
                m = m + 1

class azb30:
    """copy excel to excel"""
    def __init__(self,
                    dictconf = None,
                    mrowwscopy = None,
                    mcolumnwscopy = None,
                    pathdes= None, 
                    pathtocopy= None,
                ):
        self.__wsheetcopy = wsheetcopy
        self.__mrowwscopy = mrowwscopy
        self.__mcolumnwscopy = mcolumnwscopy
        self.__wsheetdes = wsheetdes
        self.__pathdes = pathdes
        self.__pathtocopy = pathtocopy

        app = xw.App(visible=False)
        self.desxw = xw.Book(pathdes)
        self.copyxw = xw.Book(pathtocopy)

        zab30_recor_l = dictconf["zab30_recor_l1"]

        self.__zab30_recor_l_lint = returnseplistintbbystr(zab30_recor_l)

        zab30_recor_lm = dictconf["zab30_recor_l1m"]

        self.__zab30_recor_lm_lint = returnseplistintbbystr(zab30_recor_lm)

        self.__listmaxrc = self.__zab30_recor_lm_lint + [self.__mrowwscopy]

    def copysheettoexcelexist(self, namesheet = "AZB-30"):
        """ copy sheet name  to excel existing """

        try:
            self.desxw.sheets[namesheet].delete()
            self.desxw.save()
        except:
            pass

        ws1 = self.copyxw.sheets[namesheet]
        ws1.api.Copy(Before=self.desxw.sheets['Sheet1'].api)

        my_values = self.desxw.sheets[namesheet].range('A42:V51').options(ndim=2).value 

        self.desxw.sheets['Sheet1'].range('A42:V51').value = my_values
        wb2.save()
        wb2.app.quit()

