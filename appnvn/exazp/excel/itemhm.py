from pynvn.excel import col2num
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
            valuee = self.__wsheetcopy.range(i,3).value
            print (valuee)
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