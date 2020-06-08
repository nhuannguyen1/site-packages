from openpyxl import Workbook
import openpyxl

class credict:
    """ create dict for value and key """
    def __init__ (self, wsheet = None,
                        rangea = "C7:C1000", 
                        pathfull = None, 
                        namesheet ="PTVT1", 
                        engine ="openpyxl"):
        self.wsheet = wsheet
        self.rangea = rangea
        if engine =="openpyxl":
            wb = openpyxl.load_workbook(pathfull, 
                                        read_only=True,
                                        data_only= True
                                        )
            self.ws = wb[namesheet]
        else:
            wb = xw.Book(self.fpath)
            self.ws.sheets[namesheet]

    def reindexrownotnone(self):
        """ renturn index which value not none"""
        if engine ="openpyxl":
            key_list = [cell.row for row in self.ws[self.rangea]  for cell in row if cell.value != None]
        else:
            key_list = [cell.row for cell in self.ws.range(self.rangea) if cell.value != None]
        return key_list

    def revaluerownotnone(self,rangf ="C7:C1000" ):
        """ renturn value which value not none"""
        if engine ="openpyxl":
            value_list = [cell.value for row in self.ws[rangf] for cell in row if cell.value != None ]
            
        else:
            value_list = [cell.value for cell in self.ws.range(self.rangea) if cell.value != None]

        return value_list
    def redictvaluesandvaluecol(self, columnumber = 4 ):
        """ return dict value and value column"""
        arrch = []
        res = list(zip(self.reindexrownotnone(), 
                    self.reindexrownotnone()[1:] + self.reindexrownotnone()[:1])) 
        for eler in res:
            s,t = eler
            arrchild = [self.wsheet.cell(row=ie,
                                        column = columnumber).value for ie in range(s,t) if self.wsheet.cell(row=ie,
                                                                                                            column = columnumber).value != None ]
            arrch.append(arrchild)
            arrchild = None
        dictionary = dict(zip(self.revaluerownotnone(), arrch))
        return dictionary
    
    def returndictvaluebyindexcolumnandrow(self, 
                                            value_criteria_range, 
                                            range_col ="D7:D1000", 
                                            indexcolumn = [5,6,8]):
        """ return dict by value rangce_col and indexcolumn """
        dictvalue_rangcol_indexcolumn = {}
        for value_criteria in value_criteria_range:
            indexrcevalu = [[self.valuebycol_row(cell.row,indexcolumn[0]),
                            self.valuebycol_row(cell.row,indexcolumn[1]),
                            self.valuebycol_row(cell.row,indexcolumn[2]),
                            ] for range_cell in  self.ws[range_col]\
                                                             for cell in range_cell  if  cell.value == value_criteria
                            ]
            dictvalue_rangcol_indexcolumn [value_criteria] = indexrcevalu[0]

        return dictvalue_rangcol_indexcolumn
            
    def valuebycol_row(self,irow,icolumn):
        """ return value cell by index column and row"""
        return self.wsheet.cell(row=irow,column = icolumn).value 






