from appnvn.atadctn.icontt import gui
from pynvn.authkey import authkey
from pynvn.crypt import write_key,load_key,encrypt,decrypt
class key_license:
    """ license key of app"""
    def __init__ (self, 
                    pathtokey = None,
                    pathtoserial = None,
                    product_id =7018,
                    root = None,
                    width = 400,
                    height = 300,
                    widthx = 420,
                    title = "AZB",
                    pathtovaluecsv_key = None
                    ):

        self.pathtokey = pathtokey
        self.pathtoserial = pathtoserial
        self.pathtovaluecsv_key = pathtovaluecsv_key
        self.product_id = product_id
        self.root = root
        self.width =width
        self.height =height
        self.widthx = widthx
        self.title = title

        #write_key(self.ser_key)
        key = load_key(self.pathtokey)
        try:
            valueser_key = decrypt(filename=self.pathtoserial,key = key)
        except:
            valueser_key = None
        #encrypt(filename=self.valueser_key,key = key,nametow=b"actived")
        aucre = authkey(
                        product_id=product_id,
                        key=valueser_key,
                        pathtokey = self.pathtokey,
                        pathtovaluecsv_key = pathtovaluecsv_key
                        )
        if aucre == False:
            self.guiof_inputser()
        else:
            return True

    def guiof_inputser (self):
        gui (tktk=self.root,
            pathico=None,
            width=self.width,
            height = self.height , 
            widthx=self.widthx , 
            widthy=0,
            resizable=[True,True],
            title= self.title ).setcfbs()
        self.canvas1 = tk.Canvas(self.root, 
                                width = self.width, 
                                height = self.height,
                                bg = "#5b9bd5")
        
        self.canvas1.pack()

        self.canvas1.create_text(200, 100,
                                text = "Input Serial Number",
                                fill="darkblue",
                                font="Times 20 italic bold")
            
        self.entry1 = tk.Entry (root,
                                width = 25,
                                justify = tk.CENTER,
                                font="Times 15 italic"
                                ) 
        self.canvas1.create_window(200, 140, 
                                    window=self.entry1
                                    )
        button1 = tk.Button(text='OK', 
                            command = self.getSquareRoot,
                            font="Times 15 italic")

        self.canvas1.create_window(200, 180, 
                                window=button1)
        print ("TRUE TEST")
        return self.actived 
    def getSquareRoot (self):  
        x1 = self.entry1.get()
        aucre  = authkey(
                        product_id=self.product_id ,
                        key=str(x1),
                        pathtokey = self.pathtokey,
                        pathtovaluecsv_key = self.pathtovaluecsv_key
                        )
        label1 = tk.Label(root, 
                            text= "the key is invalid or it can not be activated",
                            fg="red"
                            )
        if aucre == False:
            self.canvas1.create_window(200, 230, 
                                        window=label1)
        else:
            write_key(self.ser_key)
            key = load_key(self.ser_key)
            encrypt(filename=self.valueser_key,
                    key = key,
                    nametow=str(x1).encode('utf_8')
                    )
            self.canvas1.destroy()
            self.actived = True
            # TRUE TEST
            #self.guiforgd()
