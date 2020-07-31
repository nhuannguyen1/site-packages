import ast
import csv
def strincsvtodict(path = None):
    """ convert list in string to dict """
    reader = csv.reader(open(path, 'r'))
    return {k:ast.literal_eval(v)  for k,v in reader}

def returndictrowforcsv (path):
    """ count number of row in csv """
    with open(path, 'r') as readFile:
        listk = {lcsv[0]:lcsv[1] for lcsv in list(csv.reader(readFile, delimiter=','))}
    return listk