from pynvn.string.slist import str_seplistint_strbystr,returnliststr_from_str
from pynvn.excel import col2num,colnum_string
class vlookup:
    def __init__()
    





(loopkup_value_range = None,
            table_array = None, 
            rang_lookup = False, 
            plexcel = None,
            colum_to_get_value = None
            ):
    """usingh function vlookup"""

    cellstart = str_seplistint_strbystr(loopkup_value_range)[0]

    re_value = returnliststr_from_str(loopkup_value_range)[0]

    col_index_num = col2num(colum_to_get_value) -  col2num(re_value)  + 1

    fomularex = "=IFERROR(VLOOKUP({2},{1}!{0},{3},{4}),{5})".format(table_array,
                                                                    plexcel,
                                                                    cellstart,
                                                                    col_index_num,
                                                                    rang_lookup,
                                                                    '"' + "" + '"'
                                                                    )
    return fomularex