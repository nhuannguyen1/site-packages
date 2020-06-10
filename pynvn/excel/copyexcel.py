import openpyxl as xl
from tkinter import messagebox
from pynvn.excel.hdata import hexcel
from pynvn.path.ppath import getdirpath,refullpath
class cexcel:
    """copy excel to excel"""
    def __init__(self,sheetname = None,
                    pathdes= None, 
                    pathtocopy= None,
                    namefile="KE HOACH NGAN SACH.xlsx"
                ):

        self.sheetname = sheetname
        self.pathdes = pathdes
        self.pathtocopy = pathtocopy
        self.namefile = namefile
        # return dirpath of child folder 
        self.dirpath = getdirpath(self.pathtocopy)

    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """
        # load workbook 1
        wb1 = xl.load_workbook(filename=self.pathtocopy)
        names = wb1.sheetnames
        ws1 = wb1.worksheets[0]
        if (names[0] == "AZB-30" or  names[0] == "AZB-60"):
            exelh = hexcel(wsheet=ws1,
                        dpath=self.dirpath,
                        namefile=self.namefile)
            if names[0] == "AZB-30":                                    
                exelh.habz30()
            else:
                wbazb30 = xl.load_workbook(filename=refullpath(dirpath=self.dirpath,filename="AZB30.xlsx"))
                names = wb1.sheetnames
                exelh.habz60(wsheet_AZ30=wbazb30["AZB-30"])

            try:
                wb1.save(self.pathtocopy)
            except:
                messagebox.showerror("error","Check path for Pfile")
        # handing data AZB-60 
            
        # load workbook 2
        wb2 = xl.load_workbook(filename=self.pathdes)
        ws2 = wb2[names[0]] 
        # set data from sheet to other sheet 
        for i,row in enumerate(ws1.iter_rows()):
            for j,col in enumerate(row):
                ws2.cell(row=i+1,column=j+1).value = col.value
        try:
            wb2.save(self.pathdes)
        except IOError:
            messagebox.showerror ("error", 'File is {} still open, close it'.format(self.pathtocopy))
