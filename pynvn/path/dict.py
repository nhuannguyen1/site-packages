from pynvn.path.ppath import (
                            refullpath,
                            removeexfilename,
                            dirfolder,p_pyinstall_and_dev
                            )
from pynvn.folder.list import file_in_folder

def rdict_path(dirpath = None, 
                folderchild = "config",
                namefiles = ["logo.png","hrdata_modified.csv","conf_ex.xlsx","config_hm.xlsx","key.key","fn.csv","seri.key","ser.csv"]
                ):
    """ return dict of path """
    dict_path = {}
    for namefile in namefiles:
        keyd = folderchild + "_" + removeexfilename(namefile)
        dict_path[keyd] =  p_pyinstall_and_dev(refullpath(dirpath=dirpath,
                                            folderchild=folderchild, 
                                            filename=namefile
                                            ))
    return dict_path

def rdict_fleinfolder(dirpath = None, 
                folderchild = ["config","img"],
                ):
    """ 
    return dict of paths 
    get file in folder

    """
    rda = {}    
    for dch in  folderchild:
        dfer = dirfolder(dirNamec=dirpath,
                        subforder = dch,
                        alertexists=False
                        )
        lfname = file_in_folder(dfer)

        rd = rdict_path(dirpath=dirpath,
                    folderchild=dch,
                    namefiles=lfname)
        rda.update(rd)

    return rda