from tkinter import *
import tkinter as tk
from pynvn.path.ppath import PathFromFileNameAndDirpath
from appnvn.atadctn.indatatosel import indatagui
class selop:
    def __init__(self,tktk = None, 
                    br_image = None,
                    pathico = None,
                    br_image_path = None,
                    ):
        self.tktk = tktk
        self.br_image = br_image
        self.pathico = pathico
        self.br_image_path = br_image_path
        
        lgbr = Label (self.tktk, image = self.br_image)
        lgbr.pack()

        self.container = Frame (self.tktk,
                            bg="white")
        
        self.container.place( x = 300, 
                           y = 150)
        
    # create gui     
    def creategui(self):
        #create buttom for open file 
        button = tk.Button(self.container,text = "INPUT DATA",
                            width = 15,
                            height = 2,
                            command = lambda: indatagui(tktk=self.tktk,
                                                        br_image=self.br_image,
                                                        pathico=self.pathico,
                                                        br_image_path=self.br_image_path).creategui()
                            )
        button.pack()

        button = tk.Button(self.container,text = "CHOOSE LAYOUT",
                            width = 15,
                            height = 2,
                            command = lambda: self.donothing()
                            )
        button.pack()
        
        button = tk.Button(self.container,text = "OTHER",
                            width = 15,
                            height = 2,
                            command = lambda: self.donothing()
                            )
        button.pack()

        button = tk.Button(self.container,text = "EXIT",
                            width = 15,
                            height = 2,
                            command = lambda: self.container.quit()
                            )
        button.pack()
