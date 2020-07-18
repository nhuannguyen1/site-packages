from appnvn.atadctn.icontt import gui
from pynvn.authkey import authkey
from pynvn.crypt import write_key,load_key,encrypt,decrypt
import tkinter as tk  
class key_license:
    """ license key of app"""
    def __init__ (self,root = None,
                        pathtokey = None,
                        pathtovaluecsv_key = None,
                        ser_key = None,
                        valueser_key = None,
                        classofoject = None
                        ):
        self.root = root
        self.pathtokey = pathtokey
        self.pathtovaluecsv_key = pathtovaluecsv_key
        self.ser_key = ser_key
        self.valueser_key = valueser_key
        self.classofoject = classofoject
        key = load_key(self.ser_key)
        try:
            valueser_key = decrypt(filename=self.valueser_key,
                                    key = key)
        except:
            valueser_key = None
        #encrypt(filename=self.valueser_key,key = key,nametow=b"actived")
        aucre = authkey(
                        product_id=7018,
                        key=valueser_key,
                        pathtokey = self.pathtokey,
                        pathtovaluecsv_key = self.pathtovaluecsv_key
                        )

        if aucre == False:
            self.guiforser()
        else:
            self.classofoject.guiforgd()
    def guiforser (self):
        gui (tktk=self.root,
            pathico=None,
            width=400,
            height=300, 
            widthx=420, 
            widthy=0,
            resizable=[True,True],
            title= "AZB").setcfbs()
        self.canvas1 = tk.Canvas(self.root ,
                                width = 400, 
                                height = 300,
                                bg = "#5b9bd5")
        self.canvas1.pack()
        self.canvas1.create_text(200, 100,
                                text = "Input Serial Number",
                                fill="darkblue",
                                font="Times 20 italic bold")
        self.entry1 = tk.Entry (self.root ,
                                width = 25,
                                justify = tk.CENTER,
                                font="Times 15 italic"
                                ) 
        self.canvas1.create_window(200, 140, 
                                    window=self.entry1)

        button1 = tk.Button(text='OK', 
                            command=self.getSquareRoot,
                            font="Times 15 italic"
                            )
        self.canvas1.create_window(200, 180, 
                                    window=button1)

    def getSquareRoot (self):  
        x1 = self.entry1.get()
        #label1 = tk.Label(root, text= float(x1)**0.5)
        aucre  = authkey(
                        product_id=7018,
                        key=str(x1),
                        pathtokey = self.pathtokey,
                        pathtovaluecsv_key = self.pathtovaluecsv_key
                        )
        label1 = tk.Label(self.root, text= "the key is invalid or it can not be activated",fg="red")

        if aucre == False:
            self.canvas1.create_window(200, 230, 
                                        window=label1)
        else:
            write_key(self.ser_key)
            key = load_key(self.ser_key)
            encrypt(filename=self.valueser_key,key = key,nametow=str(x1).encode('utf_8'))
            self.canvas1.destroy()
            self.classofoject.guiforgd()
