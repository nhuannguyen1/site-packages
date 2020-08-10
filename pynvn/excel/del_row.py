from pynvn.check.list import check_list_value
from xlwings.constants import DeleteShiftDirection
from pynvn.excel import colnum_string
def delrowbyindexcell (incolumndel = "C", 
                        valueofindexcoldel = None, 
                        wb = None,
                        namesheet = None,
                        startrow =1,
                        endrow = 1000,
                        valuetoendrow = "VTC"
                        ):
    """ delete row by value of cell """
    for i in range (startrow,
                        endrow):
        valuecompare =wb.sheets[namesheet].range(i,
                                                incolumndel ).value 
        k = i
        if (valuecompare == None or valuecompare == ""):
            while True:
                wb.sheets[namesheet].range('{0}:{0}'.format(k)).api.Delete(DeleteShiftDirection.xlShiftUp)
                if (wb.sheets[namesheet].range(k,incolumndel).value != None and (wb.sheets[namesheet].range(k,incolumndel).value != "")) :
                    break
        if wb.sheets[namesheet].range(k,incolumndel).value == valuetoendrow :
            break
def delrowbyrange (incolumndel = 5, 
                        ws = None,
                        startrow =1,
                        endrow = 1000,
                        value_to_end = "VTC",
                        valuetodelete = ["",None],
                        using_value_to_end = True
                        ):
    """ delete row by value of cell """
    for i in range (startrow,endrow):
        valuecompare =ws.range(i,incolumndel ).value 
        if check_list_value(valuetocheck =[valuecompare],
                            not_in_checkvalue= False):
            while True:
                ws.range('{0}:{0}'.format(i)).api.Delete(DeleteShiftDirection.xlShiftUp)
                if check_list_value(valuetocheck=[ws.range(i,incolumndel).value]):
                    break
        if using_value_to_end:
            if ws.range(i,incolumndel).value == value_to_end :
                break
        else:
            lr = ws.range(colnum_string(incolumndel) + str(ws.cells.last_cell.row)).end('up').row
            if lr == i:
                break