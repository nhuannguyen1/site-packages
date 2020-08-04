from pynvn.string import removespace
from pynvn.excel import colnum_string
from pynvn.excel.list import lnumbercolumnbyrangstr
from pynvn.string.slist import returnseplistintbbystr
def __removespaceinrangeanan(ws = None,
                            cols= [], 
                            rows = [1,100],
                            option = "left"
                            ):
    """ remove space in excel by ws col and row """
    if len(rows) == 2:
        a,b = rows
    elif len(rows) == 1:
        a,b = rows[0],rows[0] + 1
    elif len(rows) == 0:
        lr = ws.range(colnum_string(cols[0]) + str(ws.cells.last_cell.row)).end('up').row
        a,b = 1,lr + 1
    for col in cols:
        for i in range(a,b + 1):
            valuee = ws.range(i,col).value
            if (valuee == None or valuee == ""):
                continue
            value_remove = removespace(instr=valuee,
                                        option=option
                                        )
            ws.range(i,col).value = value_remove
def removespacefromlistrange(rmrange = [], option = "both",ws = None):
    """
    rmrange: Range to remove space from csv

    """
    for rangea in rmrange:
        col_index = lnumbercolumnbyrangstr(rstr=rangea)
        row_index = returnseplistintbbystr(strint=rangea)
        __removespaceinrangeanan(ws=ws,
                                cols=col_index,
                                rows=row_index,
                                option=option
                                )