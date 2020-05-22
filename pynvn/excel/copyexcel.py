#  write to excel 
import pandas as pd
import openpyxl as xl

class cexcel:
    """copy excel to excel"""
    def __init__(self,sheetname = None,
                             pathdes= None, 
                             pathtocopy= None, 
                             ):

        self.sheetname = sheetname
        self.pathdes = pathdes
        self.pathtocopy = pathtocopy

    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """
        """
        wb1 = xl.load_workbook(filename=self.pathtocopy,read_only= True)
        names = wb1.sheetnames
        ws1 = wb1.worksheets[0]
        wb2 = xl.load_workbook(filename=self.pathdes,data_only= True)
        ws2 = wb2[names[0]] 
        for i,row in enumerate(ws1.iter_rows()):
            for j,col in enumerate(row):
                ws2.cell(row=i+1,column=j+1).value = col.value
        wb2.save(self.pathdes)
        """
        wb1 = xl.load_workbook(filename=self.pathtocopy,read_only= True)
        names = wb1.sheetnames
        ws1 = wb1.worksheets[0]
        wb=xl.Workbook(write_only=True)
        ws1=wb.create_sheet(names[0])
        for i,row in enumerate(ws1.iter_rows()):
            for j,col in enumerate(row):
                ws2.cell(row=i+1,column=j+1).value = col.value
        wb2.save(r"D:\9.AZB\20200521\0.input\out\2.xlsx")