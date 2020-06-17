def filterlistbylstr (criteria = [], liststr = []):
    """ return list filter by criteria is list str and liststr is str """
    return [elestr for elestr in liststr if any(ele in elestr for ele in criteria)]