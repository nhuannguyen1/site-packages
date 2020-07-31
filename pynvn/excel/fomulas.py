from pynvn.string.slist import str_seplistint_strbystr,returnliststr_from_str,add_sb_to_str
from pynvn.excel import col2num,colnum_string
class vlookup:
    """using function vlookup"""
    def __init__(self,loopkup_value_range = None,
                    table_array = None, 
                    rang_lookup = False, 
                    plexcel = None,
                    colum_to_get_value = None,
                    ws_des = None,
                    Sub_VLOOKUP_Locc_result_value = None,
                    lockrange = True
                    ):
        self.__ws_des = ws_des
        self.__table_array = table_array
        if lockrange:
            self.__table_array = add_sb_to_str(self.__table_array)

        self.__plexcel = plexcel
        self.__rang_lookup = rang_lookup
        self.__loopkup_value_range = loopkup_value_range
        self.__Sub_VLOOKUP_Locc_result_value = Sub_VLOOKUP_Locc_result_value
        self.__cellstart = str_seplistint_strbystr(loopkup_value_range)[0]
        re_value = returnliststr_from_str(table_array)[0]
        self.__cell_start_locvalue = str_seplistint_strbystr(Sub_VLOOKUP_Locc_result_value)[0]
        
        # index column number
        self.__col_index_num = col2num(colum_to_get_value) -  col2num(re_value)  + 1

    def valueformulas(self):

        fomularex = "=IFERROR(VLOOKUP({2},{1}!{0},{3},{4}),{5})".format(self.__table_array,
                                                                    self.__plexcel,
                                                                    self.__cellstart,
                                                                    self.__col_index_num,
                                                                    self.__rang_lookup,
                                                                    '"' + "" + '"'
                                                                    )
        return fomularex
    def forexelldes(self):
        self.__ws_des.range(self.__cell_start_locvalue).value = self.valueformulas()
        vtformulas = self.__ws_des.range(self.__cell_start_locvalue).formula
        self.__ws_des.range(self.__Sub_VLOOKUP_Locc_result_value).formula = vtformulas
