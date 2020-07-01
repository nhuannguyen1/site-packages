import re
def returnseplistintbbystr(strint):
    """ return list int by separate from string """
    return list(map(int, (re.findall('\d+', strint)))) 

def str_seplistintbbystr(strint):
    """ return list int by separate from string """
    return list(map(str, (re.findall('\w+', strint)))) 
