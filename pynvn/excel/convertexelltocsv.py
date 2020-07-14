import xlwings as xw
from pynvn.list import listpairfrom2list
from pynvn.csv.tocsv import pairlistinlisttocsv
copyxw = xw.Book(r'C:\Users\HP\Desktop\12.xlsx')
copyxws = copyxw.sheets
wsc = copyxws["Sheet3"]
def pairlistfromexcel (startrow= 1, 
                        floc = "A", 
                        sloc = "B",
                        sheet = None 
                        ):
    """ create pair list from floc and sloc of excel """
    # max row at floc 
    m_rowatfloc = sheet.range(floc + str(sheet.cells.last_cell.row)).end('up').row
    # create list from range at floc 
    listfloc = sheet.range("{0}{1}:{0}{2}".format(floc,startrow,m_rowatfloc)).value
    # create list from range at sloc 
    listsloc = sheet.range("{0}{1}:{0}{2}".format(sloc,startrow,m_rowatfloc)).value

    return listpairfrom2list(list_a=listfloc,
                            list_b=listsloc)

lissta = pairlistfromexcel(sheet=wsc)

pairlistinlisttocsv(listvalue=lissta,
                    pathcsv=r'C:\Users\HP\Desktop\12.csv')