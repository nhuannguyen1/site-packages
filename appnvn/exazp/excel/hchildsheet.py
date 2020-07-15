from pynvn.excel import (cellcoordbyvalue,
                        lcellindexbyvalue,
                        col2num,
                        valuebyindexrowcell
                        )
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
        if len (self.__valueim) != 0:
            self.lindexrow_im = lcellindexbyvalue(max_row=self.__max_row_allsheet,
                                                min_row=self.__startrow,
                                                max_col=self.__col_key_msa,
                                                min_col=self.__col_key_msa,
                                                sheet=self.__sheet_des,
                                                lvalue=self.__valueim
                                                )
        self.tranderdatasheettosheet()
        if len(self.__col_dup) !=0:
            self.hdataatdupcolumn()
    def tranderdatasheettosheet(self):
        """ transfer data formulas to another sheet """
        for abccol in self.__lcolumnformulas:
            if len (self.__valueim) != 0: 
                lvaluebyindecell_im = valuebyindexrowcell(lindexcell=self.lindexrow_im,
                                                    col=abccol,
                                                    sheet=self.__sheet_des)
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
            if len (self.__valueim) != 0: 
                self.returnvaluekeyim(cola=abccol,listvalue_im =lvaluebyindecell_im)
    def returnvaluekeyim (self,cola,listvalue_im):
        """ return value at key value from sheet copy to sheet des """
        for count,numberint in enumerate(self.lindexrow_im,0):
            self.__sheet_des.range("{0}{1}".format(cola,
                                                    numberint)).value = listvalue_im[count]
    def hdataatdupcolumn(self):
        """ h data at column index """
        for count,eles in enumerate(self.__col_dup,0):
            if len(self.__lvaluehavechild) != 0:
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
                if len (self.__valueim) != 0: 
                    lvaluebyindecell_im = valuebyindexrowcell(lindexcell=self.lindexrow_im,
                                                            col=eles,
                                                            sheet=self.__sheet_des
                                                            )

                self.__sheet_des.range("{0}{1}".format(eles,
                                                        self.__startrow)).value = self.__formulasfor_col_dup[count].format(self.__startrow)

                vtformulas = self.__sheet_des.range("{0}{1}".format(eles,self.__startrow)).formula

                self.__sheet_des.range("{0}{1}:{0}{2}".format(eles,
                                                self.__startrow,
                                                self.__max_row)).formula = vtformulas
                if len (self.__valueim) != 0: 
                    self.returnvaluekeyim(cola=eles,listvalue_im =lvaluebyindecell_im)
            