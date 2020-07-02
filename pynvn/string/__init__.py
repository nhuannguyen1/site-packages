from tkinter import messagebox
import re
import csv
import ast
def sepnumberandstrfromstr (sstr):
    """Splitting text and number in string"""
    # Splitting text and number in string 
    try:
        temp = re.compile("([a-zA-Z]+)([0-9]+)(\D)([a-zA-Z]+)([0-9]+)") 
        return temp.match(sstr).groups() 
    except:
        messagebox.showerror ("error input","Check your input {}, it must aann:aann".format(sstr))
def returnrangewolastrow(sstr):
    """Splitting text and number in string"""
    try:
        temp = re.compile("([a-zA-Z]+)([0-9]+)(\D)([a-zA-Z]+)") 
        return temp.match(sstr).group() 
    except:
        messagebox.showerror ("error input","Check your input {}, it must aann:aann".format(sstr))
def restrnotspaceifhavespace(instr = None,revalue = "None"):
    """ remove space from string"""
    return instr.replace(" ", "")

def no_accent_vietnamese(s):
    """Remove Vietnamese Accents"""
    if isinstance(s,str):
        s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
        s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
        s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
        s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
        s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
        s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
        s = re.sub(r'[ìíịỉĩ]', 'i', s)
        s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
        s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
        s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
        s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
        s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
        s = re.sub(r'[Đ]', 'D', s)
        s = re.sub(r'[đ]', 'd', s)
    return s
def converlistinstrtolist(listinstr = '["A","B" ,"C" ," D"]', path = None):
    """ convert list in string to list """
    reader = csv.reader(open(path, 'r'))
    
    return {k:ast.literal_eval(v)  for k,v in reader}