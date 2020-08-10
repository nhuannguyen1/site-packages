from pynvn.check.list import check_list_value
from xlwings.constants import DeleteShiftDirection
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
                        valuetodelete = ["",None]
                        ):
    """ delete row by value of cell """
    for i in range (startrow,endrow):
        valuecompare =ws.range(i,incolumndel ).value 
        print ("valuecompare",valuecompare)
        k = i
        if check_list_value(valuetocheck =[valuecompare],
                            not_in_checkvalue= False):
            while True:
                ws.range('{0}:{0}'.format(k)).api.Delete(DeleteShiftDirection.xlShiftUp)
                if check_list_value(valuetocheck=[ws.range(k,incolumndel).value]):
                    break
        if ws.range(k,incolumndel).value == value_to_end :
            break