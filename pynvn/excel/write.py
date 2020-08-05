from pynvn.string import removespaces
from pynvn.excel import colnum_string
from pynvn.excel.list import lnumbercolumnbyrangstr
from pynvn.string.slist import returnseplistintbbystr
from tkinter import messagebox
from pynvn.string.list import capitalizes
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
            if (valuee == None or valuee == ""):
                continue
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
    rmrange: Range to remove space from csv

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