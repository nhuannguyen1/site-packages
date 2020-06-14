class azb10:
    """copy excel to excel"""
    def __init__(self,sheetname = None,
                    pathdes= None, 
                    pathtocopy= None,
                    pathconf = None
                ):
        dicrowconf = returndictrowforcsv(path=pathconf)
        self.__azb10startr = int(dicrowconf["azb10startr"])
        #line azb10s folow row at mother
        self.__zab10_recor_l1m = int(dicrowconf["zab10_recor_l1m"])
        self.__zab10_recor_l2m = int(dicrowconf["zab10_recor_l2m"])
        self.__zab10_recor_l3m = int(dicrowconf["zab10_recor_l3m"])
        # azb10 for both
        self.__zab10_totalpaodstr = (dicrowconf["zab10_totalpaod"])
        self.__zab10_totalpaod = col2num(dicrowconf["zab10_totalpaod"])
        self.__zab10_frmpstr = (dicrowconf["zab10_frmp"])
        self.__zab10_frmp = col2num(dicrowconf["zab10_frmp"])
        self.__zab10_refundstr = (dicrowconf["zab10_refund"])
        self.__zab10_refund = col2num(dicrowconf["zab10_refund"])
        self.__zab10_efastr = (dicrowconf["zab10_efa"])
        self.__zab10_efa = col2num(dicrowconf["zab10_efa"])
        self.__zab10_finalabstr = (dicrowconf["zab10_finalab"])
        self.__zab10_finalab = col2num(dicrowconf["zab10_finalab"])

        self.__zab10_nbstr = (dicrowconf["zab10_nb"])
        self.__zab10_nb = col2num(dicrowconf["zab10_nb"])

        self.listsubtal = [self.__zab10_totalpaod,
                            self.__zab10_frmp,
                            self.__zab10_refund,
                            self.__zab10_efa,
                            self.__zab10_finalab,
                            self.__zab10_nb]

        self.listsubtalstr = [self.__zab10_totalpaodstr,
                            self.__zab10_frmpstr,
                            self.__zab10_refundstr,
                            self.__zab10_efastr,
                            self.__zab10_finalabstr,
                            self.__zab10_nbstr]
            
        
        self.indexvaluerc = [self.__zab10_recor_l1m,
                            self.__zab10_recor_l2m,
                            self.__zab10_recor_l3m]

        self.__azb10netbi =col2num (dicrowconf["azb10netbi"])
        self.sheetname = sheetname
        self.pathdes = pathdes
        self.pathtocopy = pathtocopy
        self.__Getlistsheet()
    def __Getlistsheet(self):
        self.app = xw.App(visible=False)
        self.wb1 = xw.Book(self.pathtocopy)
        self.names = self.wb1.sheets
        self.ws1 = self.wb1.sheets[self.names[0]] 
        self.wsname = self.ws1.name
        self.rows = self.ws1.api.UsedRange.Rows.count
        self.cols = self.ws1.api.UsedRange.Columns.count
        self.listmaxrc = self.indexvaluerc + [self.rows]
        # check name sheet 
    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """
        l,m = 0,0
        wb2 = xw.Book(self.pathdes)
        # Grabs the needed value
        ws2 = wb2.sheets[self.wsname]
        for i in range (self.__azb10startr, self.rows):
            valuee = self.ws1.range(i,3).value
            # value of Resource Code/Mã Tài nguyên
            valuerc = self.ws1.range(i,2).value
            if valuerc != None:
                m = self.indexvaluerc[l]
                l = l + 1
            if valuee != None:
                for j in range (1, self.cols + 1):
                    if (j in self.listsubtal) and (valuerc != None):

                        ws2.range(m,j).value = '=SUBTOTAL(9,{2}{0}:{2}{1})'.format(m + 1,
                                                                                    self.listmaxrc[l] - 1,
                                                                                    self.listsubtalstr[self.listsubtal.index(j)])
                    else:
                        ws2.range(m,j).value = self.ws1.range(i,j).value
                m = m + 1
        self.wb1.close()
        wb2.save()
        wb2.close()
        self.app.quit()