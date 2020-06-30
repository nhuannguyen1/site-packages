import re
def returnseplistintbbystr(strint):
    """ return list int by separate from string """
    return list(map(int, (re.findall('\d+', strint)))) 
