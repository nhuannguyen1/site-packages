from pynvn.excel.toexcel import toexcel
import openpyxl as xl
def returnsheet (path, namesheet = "TONG HOP HM"):
    """ return sheet name by index and path excel """
    wb1 = xl.load_workbook(filename=path)
    ws1 = wb1[namesheet]
    return ws1
def  repathlinkexcel (dpath,namefile,namesheet):
    """ return path link excel """
    pfile = "'" + dpath + "/" + "[" + namefile + "]" + namesheet + "'"
    return pfile

def colnum_string(n):
    """conver colum number become string"""
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def relistsheet(path):
    """ return all sheet of excel file """
    wb1 = xl.load_workbook(filename=path)
    names = wb1.sheetnames
    return names
def returnactivesheet(path):
    """ return active sheet """
    wb1 = xl.load_workbook(filename=path)
    sheet = wb1.active
    return sheet
def returnsheetbyname(path = None, sheetname = "PTVT"):
    """return sheet by name """
    wb1 = xl.load_workbook(filename=path)
    return wb1[sheetname]
