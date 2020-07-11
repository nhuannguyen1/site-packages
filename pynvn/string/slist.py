import re
import ast
def returnseplistintbbystr(strint):
    """ return list int by separate from string """
    return list(map(int, (re.findall('\d+', strint)))) 

def str_seplistintbbystr(strint):
    """ return list int_str by separate from string """
    return list(map(str, (re.findall('\w+', strint)))) 
def str_returnliststr (strint):
    return ast.literal_eval(strint)