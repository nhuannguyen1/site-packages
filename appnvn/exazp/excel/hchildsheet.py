from pynvn.excel import cellcoordbyvalue,lcellindexbyvalue,col2num
def hchildsheet(startrow = 1,
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
    """ Handling data sheet excell"""
    for abccol in lcolumnformulas:
        indexcol = col2num(abccol) -  col2num(col_key_msa)  + 1
        fomularex = "=IFERROR(VLOOKUP({1}{0},{2}!${1}${0}:${4}${6},{7},FALSE),{8})".format(startrow,
                                                                                        col_key_msa,
                                                                                        pfile,
                                                                                        col_key_msa,
                                                                                        columnlra[1],
                                                                                        startrow,
                                                                                        max_row_allsheet,
                                                                                        indexcol,
                                                                                        0
                                                                                        )
        sheet_des.range("{0}{1}".format(abccol,
                                        startrow)).value = fomularex
        vtformulas = sheet_des.range("{0}{1}".format(abccol,
                                                    startrow)).formula
        sheet_des.range("{0}{1}:{0}{2}".format(abccol,
                                                startrow,
                                                max_row)).formula = vtformulas

        for numberint in valueim:
            ms_des = cellcoordbyvalue(max_row=max_row_allsheet,
                                        min_row=1,
                                        max_col=col_key_msa,
                                        min_col=col_key_msa,
                                        sheet=sheet_des,
                                        valuetofile=numberint
                                        )
            ms_copy = cellcoordbyvalue(max_row=max_row_allsheet,
                                        min_row=1,
                                        max_col=col_key_msa,
                                        min_col=col_key_msa,
                                        sheet=sheet_copy,
                                        valuetofile=numberint)
            sheet_des.range("{0}{1}".format(abccol,
                                            ms_des[0])).value =sheet_copy.range("{0}{1}".format(abccol,
                                                                                                ms_copy[0])).value
    
    for count,eles in enumerate(col_dup,0):
        vtformulas = sheet_des.range("{0}{1}".format(eles,startrow + 1)).formula
        lindexrow = lcellindexbyvalue(max_row=max_row_allsheet,
                                        min_row=startrow,
                                        max_col=col_key_msa,
                                        min_col=col_key_msa,
                                        sheet=sheet_des,
                                        lvalue=lvaluehavechild
                                        )
        for index in lindexrow:
            sheet_des.range("{0}{1}".format(eles,index)).formula = formulasfor_col_dup[count].format(index)
  