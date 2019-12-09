import tkinter as TK

root = TK.Tk()
root.title('My App')
rootWidth = 768
rootHeight = 768
root.geometry("400x300")
root.resizable(width=False, height=False)

frame00 = TK.Frame(root, bd=2, relief=TK.SUNKEN)
box00 = TK.Listbox(frame00, bd=0)
frame10 = TK.Frame(root, bd=2, relief=TK.RAISED)
box10 = TK.Listbox(frame10, bd=0)

box00.grid(row=0, sticky=TK.N)
box10.grid(row=0, sticky=TK.S)
frame00.grid(row=0, column=0, sticky=TK.W)
frame10.grid(row=1, column=0, sticky=TK.W)


frame01 = TK.Frame(root, bd=2, relief=TK.SUNKEN)
box01 = TK.Listbox(frame01, bd=0)
frame11 = TK.Frame(root, bd=2, relief=TK.RAISED)
box11 = TK.Listbox(frame11, bd=0)

box01.grid(row=0, sticky=TK.N)
box11.grid(row=0, sticky=TK.S)
frame01.grid(row=0, column=1, sticky=TK.E)
frame11.grid(row=1, column=1, sticky=TK.E)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

for i in range(20):
        box00.insert(TK.END, 'test')
        box10.insert(TK.END, 'test')
        box01.insert(TK.END, 'test')
        box11.insert(TK.END, 'test')
root.mainloop()