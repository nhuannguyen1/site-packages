import os
def listfolderofpfolder(folderchild):
    """ return list folder of parent folder"""
    os.chdir(folderchild)
    lfolderp = os.listdir(folderchild)
    return lfolderp
