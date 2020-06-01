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

def relistsheet(path):
    """ return all sheet of excel file """
    wb1 = xl.load_workbook(filename=path)
    names = wb1.sheetnames
    return names
