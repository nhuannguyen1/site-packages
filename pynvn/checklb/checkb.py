import tkinter as tk
from pynvn.autoscrollbar.autoscrbar import AutoScrollbar

class ChecklistBox:
    """return check list box"""
    def __init__(self, parent, 
                choices = ["Nhuan", "Hong"], 
                i = 0,
                onvalue = True,
                offvalue = "" ,
                width = 60,
                listsheetname = None,
                **kwargs):
        self.choices = choices
        self.onvalue = onvalue
        self.offvalue = offvalue
        self.parent = parent
        self.vars = []
        self.i = i
        self.width = width
        self.listsheetname = listsheetname
        self.i = 1
        self.rechecklistbox()

    def rechecklistbox (self):
        """ return check list box from arr """
        for idx,choice in enumerate(self.choices):
            var = tk.StringVar()
            varsn = tk.StringVar(value=self.listsheetname[idx])
            self.vars.append(var)
            lb = tk.Label (self.parent,
                                text = "File Name _ sheet Name",
                                bg = "white")
            lb.grid(row=0,
                    column=0, 
                    sticky =  tk.W) 

            cb = tk.Checkbutton(self.parent, 
                                var=var, 
                                text=choice + "_ Sheet name: " + self.listsheetname[idx] ,
                                onvalue=choice,
                                offvalue=self.offvalue,
                                anchor=tk.W, 
                                width = int (self.width/2) ,
                                bg = "white",
                                relief="flat", 
                                highlightthickness=0
                                )
            cb.grid(row=self.i,
                        column=0, 
                        sticky =  tk.NSEW) 

            lb1 = tk.Label (self.parent,
                            bg = "white",
                            text = "Caculate")
            lb1.grid(row=0,column=1, 
                            sticky =  tk.NSEW) 
            cbs = tk.Checkbutton(self.parent, 
                                var=varsn, 
                                onvalue=self.listsheetname[idx],
                                offvalue=self.offvalue,
                                width = int (self.width/2) - 2,
                                bg = "white",
                                relief="flat", 
                                justify = tk.RIGHT,
                                highlightthickness=0
                                )
            cbs.grid(row=self.i,
                        column=1, 
                        sticky =  tk.E) 
            self.i = self.i + 1
    def getCheckedItems(self):
        values = []
        for var in self.vars:
            value =  var.get()
            if value:
                values.append(value)
        return values        