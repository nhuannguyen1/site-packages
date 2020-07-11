def listbyrangeremoveduplicate(sheetexcel,rangea):
    """ return list excel remove duplicate"""
    return list(set(sheetexcel.range(rangea).value))