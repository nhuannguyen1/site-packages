from pynvn.excel.copypasteexell import cprange
import xlwings as xw
from pynvn.csv.rcsv import returndictrowforcsv
class crangeactive:
    """ copy sheet and change value cell """
    def __init__(self,pathconf):
        # call dict 
        dictconf = returndictrowforcsv(path=pathconf)

