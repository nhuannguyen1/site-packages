import tkinter as tk

class AutoScrollbar(tk.Scrollbar): 

    """ Defining set method with all  """
    # its parameter 
    
    def set(self, low, high): 

        if float(low) <= 0.0 and float(high) >= 1.0: 

            # Using grid_remove 

            self.tk.call("grid", "remove", self) 

        else: 

            self.grid() 

        tk.Scrollbar.set(self, low, high) 
