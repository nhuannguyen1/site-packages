from appnvn.atadctn.icontt import gui
import tkinter as tk
class sgui:
    """ interface to input serial licence """
    def __init__ (self, root = None, 
                        width = 400, 
                        height = 300,
                        widthx = 550, 
                        widthy = 0,
                        au_creater = "Creator: Mr.Hoàng + Mr.Đồng",
                        textaupro = "Programmer: Mr. Nhuần - nhuannv.vs@gmail.com",
                        titlesw = "AZBNS V01"
                    ):
        self.root = root
        self.au_creater = au_creater
        self.textaupro = textaupro
        self.titlesw = titlesw
        gui (tktk=root,
            pathico=None,
            width=width,
            height=height, 
            widthx=widthx, 
            widthy=widthy,
            resizable=[0,0],
            title= titlesw).setcfbs()

    def guiforser(self):
        """ gui for input licence key """
        self.canvas1 = tk.Canvas(self.root ,
                                width = 400, 
                                height = 300,
                                bg = "#5b9bd5")
        self.canvas1.pack()
        self.canvas1.create_text(200, 100,
                                text = "Input your key below:",
                                fill="darkblue",
                                font="Times 20 italic bold")
        self.entry1 = tk.Entry (self.root ,
                                width = 35,
                                justify = tk.CENTER,
                                font="Times 15 italic"
                                ) 
        self.canvas1.create_window(200, 140, 
                                    window=self.entry1)

        button1 = tk.Button(text='OK', 
                            font="Times 15 italic"
                            )
        self.canvas1.create_window(200, 180, 
                                    window=button1)

        self.canvas1.create_text(13, 250,
                                text = self.au_creater,
                                fill="darkblue",
                                anchor = "w",
                                font="Times 13 italic")

        self.canvas1.create_text(13, 280,
                                text = self.textaupro,
                                fill="darkblue",
                                anchor = "w",
                                font="Times 13 italic")
root = tk.Tk ()
obj = sgui(root).guiforser()
root.mainloop()