from pynvn.string import removespace
from pynvn.excel import colnum_string
from pynvn.excel.list import lnumbercolumnbyrangstr
from pynvn.string.slist import returnseplistintbbystr
from tkinter import messagebox
from pynvn.string.list import capitalizefs
def __vcell(ws = None,
            cols= [], 
            rows = [1,100],
            option = "left",
            option_fun = "removespace"
            ):
    """ remove space in excel by ws col and row """
    if len(rows) == 2:
        a,b = rows
    elif len(rows) == 1:
        a,b = rows[0],rows[0] + 1
    elif len(rows) == 0:
        lr = ws.range(colnum_string(cols[0]) + str(ws.cells.last_cell.row)).end('up').row
        a,b = 1,lr + 1
    else:
        messagebox.showerror("Error", "Not find for this case rows: {0}".format(rows))
    for col in cols:
        for i in range(a,b + 1):
            valuee = ws.range(i,col).value
            if (valuee == None or valuee == ""):
                continue
            if option_fun == "removespace":
                nvalue = removespace(instr=valuee,
                                        option=option
                                        )
            elif option_fun == "capfs":
                nvalue = capitalizefs(instr=valuee)
            ws.range(i,col).value = nvalue

def hvalues_in_cell(rmrange = [], 
                    option = "both",
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
