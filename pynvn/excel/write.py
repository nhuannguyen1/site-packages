from pynvn.string import removespaces
from pynvn.excel import colnum_string
from pynvn.excel.list import lnumbercolumnbyrangstr
from pynvn.string.slist import returnseplistintbbystr
from tkinter import messagebox
from pynvn.string.list import capitalizes
from pynvn.excel.del_row import delrowbyrange
def __vcell(ws = None,
            cols= [], 
            rows = [1,100],
            option = [],
            option_fun = "removespace"
            ):
    """ remove space in excel by ws col and row """
    a,b = _startrow_endrow(ws=ws,
                            rows=rows,
                            cols=cols)
    for col in cols:
        for i in range(a,b + 1):
            valuee = ws.range(i,col).value
            myDictfun = {
                        "removespace": (lambda : removespaces(instr=valuee,
                                                                options=option)),
                        "capfs": (lambda : capitalizes(instr=valuee,
                                                        options=option)),                              
                        }
            nvalue = myDictfun[option_fun]()
            ws.range(i,col).value = nvalue

def hvalues_in_cell(rmrange = [], 
                    option = [],
                    ws = None,
                    option_fun = "removespace"
                    ):

    """
    rmrange: Range to handling string: \n
    ex: A1, A1:B3
    ws: worksheet corresponds to the rmrange \n
    option: style to  handling:\n
    ex: tspacetoospace, fs,upper_all,,both, left, right \n
    option_fun: For case function "REMOVESPACE" user select from interface \n
    ex: removespace,capfs
    """
    for rangea in rmrange:
        __vcell(ws=ws,
                cols=lnumbercolumnbyrangstr(rstr=rangea),
                rows=returnseplistintbbystr(strint=rangea),
                option= option,
                option_fun= option_fun
                )

def _startrow_endrow(ws = None, 
                    rows = [],
                    cols = []
                    ):
    """ return start row and end row """

    if len(rows) == 2:
        return rows
    elif len(rows) == 1:
        return [rows[0],rows[0] + 1]
    elif len(rows) == 0:
        lr = ws.range(colnum_string(cols[0]) +\
            str(ws.cells.last_cell.row)).end('up').row
        return [1,lr + 1]
    else:
        messagebox.showerror("Error",
                             "Not find for this case rows: {0}".format(rows))

class hrangesheet:
    """ 
    handling range for sheet\n
    rmrange: Range to handling string: \n
    ex: A1, A1:B3,A
    ws: worksheet corresponds to the rmrange \n
    option: style to  handling:\n
    ex: tspacetoospace, fs,upper_all,both, left, right,lower_all,all \n
    option_fun: For case function "REMOVESPACE or CAPFS" user select from interface \n
    ex: REMOVESPACE,CAPFS
    """
    def __init__(self,
                rmrange = [], 
                option = [],
                ws = None,
                option_fun = "removespace",
                feature_fun = "hstr",
                **kw
                    ):
        self.__option = option
        self.__ws = ws
        self.__option_fun = option_fun
        self.__feature_fun = feature_fun
        for rangea in rmrange:
            self.__cols=lnumbercolumnbyrangstr(rstr=rangea)
            self.__rows=returnseplistintbbystr(strint=rangea)
            self.__vcell(**kw)

    def __vcell(self,**kw):
        """ 
        remove space in excel by ws col and row 
        """
        a,b = _startrow_endrow(ws=self.__ws,
                                rows=self.__rows,
                                cols=self.__cols
                                )
        for col in self.__cols:
            if self.__feature_fun == "hstr":
                hstr_in_range(st_row=a,
                                end_row = b,
                                index_col=col,
                                option=self.__option,
                                ws=self.__ws,
                                option_fun = self.__option_fun
                            )
            else:
                delrowbyrange(incolumndel=col,
                                ws=self.__ws,
                                startrow=a,
                                endrow=b,**kw)
        
def hstr_in_range(st_row, 
                    end_row,
                    index_col,
                    option = [],
                    ws = None,
                    option_fun = None
                ):
    """
    handling string in range 
    st_row: start row  sheet 
    end_row: end row  sheet 
    ws: worksheet input 
    option: style to  handling:\n
    ex: tspacetoospace, fs,upper_all,both, left, right,lower_all,all \n  
    option_fun: For case function "REMOVESPACE or CAPFS" user select from interface \n
    """
    for i in range(st_row,end_row + 1): 
        valuee = ws.range(i,index_col).value
        myDictfun = {
                    "removespace": (lambda : removespaces(instr=valuee,
                                                        options=option)),
                    "capfs": (lambda : capitalizes(instr=valuee,
                                                    options=option)),                              
                    }
        nvalue = myDictfun[option_fun]()
        ws.range(i,index_col).value = nvalue