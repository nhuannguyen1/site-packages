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
                **kwargs):
        self.choices = choices
        self.onvalue = onvalue
        self.offvalue = offvalue
        self.parent = parent
        self.vars = []
        self.i = i
        self.width = width
        self.rechecklistbox()
    def rechecklistbox (self):
        """ return check list box from arr """
        for choice in self.choices:
            if ".xlsx" in choice:
                var = tk.StringVar(value=choice)
                self.vars.append(var)
                cb = tk.Checkbutton(self.parent, 
                                    var=var, 
                                    text=choice,
                                    onvalue=choice,
                                    offvalue=self.offvalue,
                                    anchor=tk.W, 
                                    width = self.width ,
                                    bg = "white",
                                    relief="flat", 
                                    highlightthickness=0
                                    )
                cb.grid(row=self.i,column=0, sticky =  tk.NSEW) 
                self.i = self.i + 1

    def getCheckedItems(self):
        values = []
        for var in self.vars:
            value =  var.get()
            if value:
                values.append(value)
        return values