import tkinter as TK
class GuiTk (TK.Tk):
    def __init__(self,*args,**kwargs):
        TK.Tk.__init__(self,*args,**kwargs)
        self.title("Use button")
        self.geometry("400x400")
        self.frame1 = TK.Frame (self, bg='cyan',width=200, height=200, borderwidth=1, relief=TK.RAISED)
        self.frame1.grid(row = 0,column = 0,sticky="nsew")
        TK.Label(self.frame1, text = 'Model Dimensions').grid(row = 0, column = 0,columnspan = 1,sticky="w")
        TK.Label(self.frame1, text = 'Width:').grid(row = 1, column = 0)
        TK.Label(self.frame1, text = 'Length:').grid(row = 1, column = 1)

        self.frame2 = TK.Frame(self, bg='cyan',width=200, height=200, borderwidth=1, relief=TK.RAISED )
        self.frame2.grid(column=1, row=0, sticky="nsew")
        TK.Button(self.frame2, text="Simple button").grid(row = 0, column = 0,sticky="nsew")
        TK.Button(self.frame2, text="Simple button1").grid(row = 0, column = 1)
        TK.Button(self.frame2, text="Simple button2").grid(row = 1, column = 0,columnspan=2,sticky="we",pady= 0)

app = GuiTk()
app.mainloop()