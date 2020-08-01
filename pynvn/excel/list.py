from pynvn.list import listpairfrom2list,convertoint_ifisfloat

def listbyrangeremoveduplicate(sheetexcel,rangea):
    """ return list excel remove duplicate"""
    return list(set(sheetexcel.range(rangea).value))

def listbyrange(sheetexcel,rangea,removeduplicate = False):
    """ return list excel by range"""
    if removeduplicate:
        return list(set(sheetexcel.range(rangea).value))
    else:
        return sheetexcel.range(rangea).value

def pairslistfromexcel (startrow= 1, 
                        floc = "A", 
                        sloc = "B",
                        convetfloattointat_slot = True,
                        sheet = None,
                        ):
    """ create pair list from floc and sloc of excel """
    # max row at floc 
    m_rowatfloc = sheet.range(floc + str(sheet.cells.last_cell.row)).end('up').row
    # create list from range at floc 
    listfloc = sheet.range("{0}{1}:{0}{2}".format(floc,startrow,m_rowatfloc)).value
    # create list from range at sloc 
    listsloc = sheet.range("{0}{1}:{0}{2}".format(sloc,startrow,m_rowatfloc)).value
    if convetfloattointat_slot:
        listsloc = convertoint_ifisfloat(listsloc)
        
    return listpairfrom2list(list_a=listfloc,
                            list_b=listsloc)

def removevalueinlistpair(lista,
                        deleteifvalue = [None,""],
                        lower_index_0 = True):
    """
    remove value in list pair by list deleteifvalue 
    """

    if lower_index_0:
        listpair = [[pairarr[0].lower(),pairarr[1]] for pairarr in lista if pairarr[0] not in deleteifvalue]
    else:
        listpair = [pairarr for pairarr in lista if pairarr[0] not in deleteifvalue]

    return listpair
