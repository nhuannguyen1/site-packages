import ast
import csv
import re
def strincsvtodict(path = None):
    """ convert list in string to dict """
    reader = csv.reader(open(path, 'r'))
    return {k:ast.literal_eval(v)  for k,v in reader}

def returndictrowforcsv (path):
    """ count number of row in csv """
    with open(path, 'r') as readFile:
        listk = {lcsv[0]:lcsv[1] for lcsv in list(csv.reader(readFile, delimiter=','))}
    return listk


def dict_str_fromlist(path = None):
    """ 
    convert list in string to dict 
    ex: csv content: "r,A1,A2,A3" ---> dict: {r: ["A1","A2","A3"}
    
    """
    reader = csv.reader(open(path, 'r'))
    return {k:re.split("[,]", v)  for k,v in reader}


def dict_from_csv2col (path):
    """ count number of row in csv """
    with open(path, 'r') as readFile:
        listk = {lcsv[0]:lcsv[1] for lcsv in list(csv.reader(readFile, delimiter=','))}
    return listk