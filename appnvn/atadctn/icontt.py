from tkinter import messagebox

class gui:
    """set logo and size window of widget """
    def __init__(self,tktk = None, 
                        pathico = None,
                        width = None, 
                        height = None,
                        widthx = None ,
                        widthy = None,
                        resizable =[0,0] ):

        self.tktk = tktk
        self.pathico = pathico
        self.width = width
        self.height = height
        self.widthy = widthy
        self.widthx = widthx
        self.resizable = resizable
    
    def setcfbs (self):
        
        fkv = self.findkeyvalue()
        self.setsw(fkv)
        self.call(fkv,5)
        
        self.tktk.resizable(self.resizable [0], 
                            self.resizable [1])
                            
        self.tktk.iconbitmap(self.pathico)
        self.tktk.title ("ATAD STEEL STRUCTURE CORPORATION")

    def center(self):
        """set calulate for widget to center window"""
        self.widthx = (self.tktk.winfo_screenwidth() // 2) - (self.width // 2)
        self.widthy = (self.tktk.winfo_screenheight() // 2) - (self.height // 2)
       
    def setsw(self,keyvalue):
        self.functions = {
                    'nnnn':lambda x: self.resnnnn(),
                    'ccoo':lambda x: self.resccoo(),
                    'ccnn':lambda x: self.resccnn(),
                    '*': self.other_case,
                    }

    def resnnnn (self):
        """resturn result of nnnn """
        self.tktk.geometry ("{}x{}+{}+{}".format(self.width,
                                                self.height,
                                                self.widthx,
                                                self.widthy
                                                ))
    
    def resccoo(self):
        """resturn result of ccoo """
        # Gets the requested values of the height and widht.
        windowWidth  = self.tktk.winfo_reqwidth()
        windowWidth = self.tktk.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.tktk.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.tktk.winfo_screenheight()/2 - windowWidth/2) 

        self.tktk.geometry("+{}+{}".format(positionRight,
                                            positionDown))

    def resccnn(self):
        """resturn result of ccnn """
        self.center()
        self.tktk.geometry ("{}x{}+{}+{}".format(self.width,
                                                self.height,
                                                self.widthx,
                                                self.widthy
                                                ))

    def other_case(self,x):

       messagebox.showerror("error"," not yes case this")
    
    def findkeyvalue(self):
        """find key value """
        if self.widthx != "center" and self.widthy != "center" and self.width !=None and  self.height !=None: return "nnnn"
        
        elif self.widthx == "center" and self.widthy == "center" and self.width ==None and  self.height ==None:return "ccoo"

        elif self.widthx == "center" and self.widthy == "center" and self.width !=None and  self.height !=None:return "ccnn"
        else: return "*"
    
    def call(self,keyvaluee, x):
        return self.functions[keyvaluee](x)