from pynvn.string import removespaces
from pynvn.excel import colnum_string
from pynvn.excel.list import lnumbercolumnbyrangstr
from pynvn.string.slist import returnseplistintbbystr
from tkinter import messagebox
from pynvn.string.list import capitalizes
from pynvn.excel.del_row import delrowbyrange

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

class hstr_ex(object):
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
    def __init__(self,f):
        self.f = f
    def __call__(self,*args, **kwargs):
        ws = kwargs["ws"]
        rmrange = kwargs["rmrange"]
        options = kwargs["option"]
        for rangea in rmrange:
            cols=lnumbercolumnbyrangstr(rstr=rangea)
            rows=returnseplistintbbystr(strint=rangea)
            a,b = _startrow_endrow(ws=ws,
                                    rows=rows,
                                    cols=cols
                                    )
            for col in cols:
                for i in range(a,b + 1):
                    instr = ws.range(i,col).value
                    if (instr == "" or instr ==None):
                        pass
                    else:
                        for option in options:
                            instr = self.f(instr=instr,
                                        option=option
                                        )
                        ws.range(i,col).value = instr