import os
def listfileofpfolder(folderchild, fmnamefile = ["jpg","gif"]):
    """ return list file of p folder"""
    os.chdir(folderchild)
    lfiles = os.listdir(folderchild)
    lfileinforders = [lfile for lfile in lfiles if any(n in lfile for n in fmnamefile)]
    return lfileinforders
