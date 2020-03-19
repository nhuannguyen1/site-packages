
class gui:
    def __init__(self,tktk = None, pathico = None,width = 0, height = 0,widthx = 0 ,widthy = 0,resizable =[0,0] ):
    # set logo and title 
        self.tktk = tktk
        self.pathico = pathico
        self.width = width
        self.height = height
        self.widthy = widthy
        self.widthx = widthx
        self.resizable = resizable

    def setcfbs (self):
        self.tktk.geometry ("{}x{}+{}+{}".format(self.width,
                                                self.height,
                                                self.widthx,
                                                self.widthy
                                                )
                                                )
        self.tktk.resizable(self.resizable [0], 
                            self.resizable [1]
                            )
                            
        self.tktk.iconbitmap(self.pathico)
        self.tktk.title ("ATAD STEEL STRUCTURE CORPORATION")
