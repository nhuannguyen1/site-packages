def listbyrangeremoveduplicate(sheetexcel,rangea):
    """ return list excel remove duplicate"""
    return list(set(sheetexcel.range(rangea).value))
def listbyrange(sheetexcel,rangea,removeduplicate = False):
    """ return list excel by range"""
    if removeduplicate:
        return list(set(sheetexcel.range(rangea).value))
    else:
        return sheetexcel.range(rangea).value
