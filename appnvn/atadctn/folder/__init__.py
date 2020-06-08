from pynvn.list.str import exstrtolistint
def returnlistfolderbywh(foldernamelist,
                        width_p,
                        height_p):
    """ return list folder by w and h """
    listfolder = []
    for folderch in foldernamelist:
        # extract w, h from folder name 
        w, h = exstrtolistint (folderch)
        if (w < width_p and h < height_p):
            listfolder.append (folderch)
    return listfolder 
