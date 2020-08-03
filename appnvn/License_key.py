from appnvn.atadctn.icontt import gui
from pynvn.authkey import authkey
from pynvn.crypt import (write_key,
                        load_key,
                        encrypt,
                        decrypt
                        )
import tkinter as tk  
def key_license (tktk = None,
                    pathtokey = None,
                    pathtovaluecsv_key = None,
                    ser_key = None,
                    valueser_key = None,
                    product_id = 7018,
                    **kw
                    ):
    """ 
    license key of app
    check valid key (valid or invalid)
    """

    key = load_key(ser_key)
    try:
        valueser_key_de = decrypt(filename=valueser_key,
                                    key = key)
    except:
        valueser_key_de = None

    aucre = authkey(
                    product_id=product_id,
                    key=valueser_key_de,
                    pathtokey = pathtokey,
                    pathtovaluecsv_key = pathtovaluecsv_key
                    )
    if aucre[0] == False:
        guiforser(tktk=tktk,
                pathtokey =pathtokey,
                pathtovaluecsv_key= pathtovaluecsv_key,
                ser_key = ser_key,
                valueser_key = valueser_key,
                product_id = product_id,
                **kw
                )
    else:
        return True

def guiforser (tktk = None,
                pathico = None,
                width= 400,
                height = 300,
                widthx = 550,
                widthy = 0,
                titlegui = "Fapp",
                pathtokey = None,
                pathtovaluecsv_key = None,
                valueser_key = None,
                ser_key = None,
                product_id = None,
                au_creator =  "Creator: Mr.Hoàng + Mr.Đồng",
                au_Programmer = "Programmer: Mr. Nhuần - nhuannv.vs@gmail.com"
                ):
    gui (tktk=tktk,
            pathico=pathico,
            width=width,
            height=height, 
            widthx=widthx, 
            widthy=widthy,
            resizable=[0,0],
            title= titlegui).setcfbs()
    canvas1 = tk.Canvas(tktk ,
                        width = 400, 
                        height = 300,
                        bg = "#5b9bd5")
    canvas1.pack()
    canvas1.create_text(200, 100,
                                text = "Input your key below:",
                                fill="darkblue",
                                font="Times 20 italic bold")
    entry1 = tk.Entry (tktk ,
                        width = 35,
                        justify = tk.CENTER,
                        font="Times 15 italic"
                        ) 
    canvas1.create_window(200, 140, 
                            window=entry1)

    button1 = tk.Button(text='OK', 
                        command=lambda: _checkvalidkey(tktk = tktk,
                                                        entry1=entry1,
                                                        canvas1=canvas1,
                                                        pathtokey=pathtokey,
                                                        pathtovaluecsv_key=pathtovaluecsv_key,
                                                        valueser_key = valueser_key,
                                                        ser_key = ser_key,
                                                        product_id=product_id
                                                        ),
                        font="Times 15 italic"
                        )
    canvas1.create_window(200, 180, 
                            window=button1)

    canvas1.create_text(13, 250,
                            text = au_creator,
                            fill="darkblue",
                            anchor = "w",
                            font="Times 13 italic")

    canvas1.create_text(13, 280,
                            text = au_Programmer,
                            fill="darkblue",
                            anchor = "w",
                            font="Times 13 italic")

def _checkvalidkey (tktk,
                    entry1,
                    canvas1,
                    pathtokey,
                    pathtovaluecsv_key,
                    valueser_key,
                    ser_key,
                    product_id = None
                    ):
    """ check valid key """
    x1 = entry1.get()
    aucre  = authkey(
                    product_id=product_id,
                    key=str(x1),
                    pathtokey = pathtokey,
                    pathtovaluecsv_key = pathtovaluecsv_key
                    )
    label1 = tk.Label(tktk, 
                    text= "the key is invalid or it can not be activated",
                    fg="red")

    if aucre[0] == False:
        canvas1.create_window(200, 230, window=label1)
    else:
        write_key(ser_key)
        key = load_key(ser_key)
        encrypt(filename=valueser_key,
                    key = key,
                    nametow=str(x1).encode('utf_8'))
        tk.messagebox.showinfo("Activation Wizard",
                                "Activation successful, License expires: " + aucre[1] )
        tktk.quit()
