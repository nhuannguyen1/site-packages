import openpyxl as xl
from tkinter import messagebox
from pynvn.excel.hdata import hexcel
from pynvn.path.ppath import getdirpath,refullpath
class cexcel:
    """copy excel to excel"""
    def __init__(self,sheetname = None,
                    pathdes= None, 
                    pathtocopy= None,
                    namefile="KE HOACH NGAN SACH.xlsx",
                    namesheetchild = "AZB"
                ):

        self.sheetname = sheetname
        self.pathdes = pathdes
        self.pathtocopy = pathtocopy
        self.namefile = namefile
        self.namesheetchild = namesheetchild\
        self.__Getlistsheet()
    def __Getlistsheet(self):
        self.dirpath = getdirpath(self.pathtocopy)
        self.wb1 = xl.load_workbook(filename=self.pathtocopy)
        self.names = wb1.sheetnames
        self.ws1 = wb1[self.names[0]]
        # check name sheet 
        if self.namesheetchild  in self.names[0]:
            pass
        else:
            messagebox.showerror("error", 
                                "Name sheet must start \
                                from symbols {}...".format(self.namesheetchild))

    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """ 
        # load workbook 2
        wb2 = xl.load_workbook(filename=self.pathdes)
        ws2 = wb2[self.names[0]] 
        # set data from sheet to other sheet 
        """
        for i,row in enumerate(self.ws1.iter_rows()):
            for j,col in enumerate(row):
                ws2.cell(row=i+1,column=j+1).value = col.value
        """

        # copying the cell values from source  
        # excel file to destination excel file 
        for i in range (43, mr + 1): 
            if self.ws1.cell(row = i, column = 2) == "":
                for j in range (1, mc + 1): 
                    n = 0
                    k = i 
                    # reading cell value from source excel file 
                    c = self.ws1.cell(row = i, column = j) 
                    # writing the read value to destination excel file 
                    ws2.cell(row = k, column = j).value = c.value 



        try:
            wb2.save(self.pathdes)
        except:
            messagebox.showerror ("error", 'File is {} still open,\
                                             close it'.format(self.pathtocopy))