from openpyxl import Workbook
import openpyxl

class credict:
    """ create dict for value and key """
    def __init__ (self, wsheet = None,
                        rangea = "C7:C1000", 
                        pathfull = None, 
                        namesheet ="PTVT1"):
        self.wsheet = wsheet
        self.rangea = rangea
        wb = openpyxl.load_workbook(pathfull, read_only=True,data_only= True)
        self.ws = wb[namesheet]
    def reindexrownotnone(self):
        """ renturn index which value not none"""
        key_list = []
        for row in self.ws[self.rangea]:
            for cell in row:
                if cell.value != None:
                    key_list.append(cell.row)
        return key_list
    def revaluerownotnone(self):
        """ renturn value which value not none"""
        value_list = []
        for row in self.ws[self.rangea]:
            for cell in row:
                if cell.value != None:
                    value_list.append(cell.value)
        return value_list

    def redictvaluesandvaluecol(self, columnumber = 4 ):
        """ return dict value and value column"""
        arrch = []
        arrchild = []
        res = list(zip(self.reindexrownotnone(), 
                    self.reindexrownotnone()[1:] + self.reindexrownotnone()[:1])) 
        for eler in res:
            s,t = eler[0],eler[1] 
            for ie  in  range (s,t):
                value1 = self.wsheet.cell(row=ie,column = columnumber).value
                if value1 != None:
                    arrchild.append(value1)
                
            arrch.append(arrchild)
            arrchild = []
        dictionary = dict(zip(self.revaluerownotnone(), arrch))
        return dictionary
