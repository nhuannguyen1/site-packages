from pynvn.excel import cellcoordbyvalue,lcellindexbyvalue,col2num
class hchildsheet:
    """ h data at sheet child of azb """
    def __init__(self,
                startrow = 1,
                col_key_msa = None,
                pfile = None, 
                columnlra = None,
                max_row = 100, 
                max_col = 20, 
                lcolumnformulas = None, 
                valueim = None,
                sheet_des = None,
                sheet_copy = None, 
                col_dup = None,
                lvaluehavechild = None,
                max_row_allsheet= 1000,
                formulasfor_col_dup = None):
        self.__startrow = startrow
        self.__col_key_msa = col_key_msa
        self.__pfile = pfile
        self.__columnlra = columnlra
        self.__max_row = max_row
        self.__max_col = max_col
        self.__lcolumnformulas = lcolumnformulas
        self.__valueim = valueim
        self.__sheet_des = sheet_des
        self.__sheet_copy = sheet_copy
        self.__lvaluehavechild = lvaluehavechild
        self.__max_row_allsheet = max_row_allsheet
        self.__formulasfor_col_dup = formulasfor_col_dup
        self.__col_dup = col_dup

    def tranderdatasheettosheet(self):
        """ transfer data formulas to another sheet """
        for abccol in self.__lcolumnformulas:
            indexcol = col2num(abccol) -  col2num(self.__col_key_msa)  + 1
            fomularex = "=IFERROR(VLOOKUP({1}{0},{2}!${1}${0}:${4}${6},{7},FALSE),{8})".format(self.__startrow,
                                                                                        self.__col_key_msa,
                                                                                        self.__pfile,
                                                                                        self.__col_key_msa,
                                                                                        self.__columnlra[1],
                                                                                        self.__startrow,
                                                                                        self.__max_row_allsheet,
                                                                                        indexcol,
                                                                                        0
                                                                                        )
            self.__sheet_des.range("{0}{1}".format(abccol,
                                        self.__startrow)).value = fomularex
            vtformulas = self.__sheet_des.range("{0}{1}".format(abccol,
                                                    self.__startrow)).formula
            self.__sheet_des.range("{0}{1}:{0}{2}".format(abccol,
                                                self.__startrow,
                                                self.__max_row)).formula = vtformulas
    def returnvaluekeyim (self):
        """ return value at key value from sheet copy to sheet des """
        for abccol in self.__lcolumnformulas:
            for numberint in self.__valueim:
                ms_des = cellcoordbyvalue(max_row=self.__max_row_allsheet,
                                            min_row=1,
                                            max_col=self.__col_key_msa,
                                            min_col=self.__col_key_msa,
                                            sheet=self.__sheet_des,
                                            valuetofile=numberint
                                        )
                ms_copy = cellcoordbyvalue(max_row=self.__max_row_allsheet,
                                            min_row=1,
                                            max_col=self.__col_key_msa,
                                            min_col=self.__col_key_msa,
                                            sheet=self.__sheet_copy,
                                            valuetofile=numberint
                                            )
                self.__sheet_des.range("{0}{1}".format(abccol,
                                            ms_des[0])).value = self.__sheet_copy.range("{0}{1}".format(abccol,
                                                                                                ms_copy[0])).value
    def hdataatdupcolumn(self):
        """ h data at column index """
        for count,eles in enumerate(self.__col_dup,0):
            if self.__lvaluehavechild != None:
                lindexrow = lcellindexbyvalue(max_row=self.__max_row_allsheet,
                                            min_row=self.__startrow,
                                            max_col=self.__col_key_msa,
                                            min_col=self.__col_key_msa,
                                            sheet=self.__sheet_des,
                                            lvalue=self.__lvaluehavechild
                                            )
                for index in lindexrow:
                    self.__sheet_des.range("{0}{1}".format(eles,index)).formula = self.__formulasfor_col_dup[count].format(index)
            else:
                self.__sheet_des.range("{0}{1}".format(eles,self.__startrow)).value = self.__formulasfor_col_dup[count].format(self.__startrow)
                vtformulas = self.__sheet_des.range("{0}{1}".format(eles,self.__startrow)).formula
                self.__sheet_des.range("{0}{1}:{0}{2}".format(eles,
                                                self.__startrow,
                                                self.__max_row)).formula = vtformulas