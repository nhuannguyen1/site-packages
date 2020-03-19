class loginatad:
    "input user and password to sw"
    def __init__ (self,uname= None,pass_ = None):
        self.uname = uname
        self.pass_ = pass_
    # check user and password when login 
    def login (self):
        if self.uname.get() =="" or self.pass_.get() =="":
            messagebox.showerror ("Error",
                                "All fields are required !!")
                
        elif self.uname.get() =="nhuan" and self.pass_.get() =="1234":
            messagebox.showinfo ("successfull",
                                f" wellcome{self.uname.get()}")

        else:
            messagebox.showerror ("Error",
                                "invalid username or password")
                                