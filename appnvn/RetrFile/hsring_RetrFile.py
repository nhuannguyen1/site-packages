from pynvn import dict_str_from_lcsv
from pynvn.excel import (sheet_by_namesheet,
                        activesheet
                        )
from pynvn import filter_lstr
from pynvn.excel.write import hvalues_in_cell
class rapp:
    """ 
    Generic class for this template with variables\n
    retr_path: directory of execute excel file\n
    retr_sheetname: name of sheet name of retr_path excel\n
    fuction: choose the feature  want to use \n
    pathconf: Directory of path conf (.csv), this path have conf parameter 

    """
    def __init__(self,
                retr_path = None,
                retr_sheetname =None, 
                fuction = None,
                pathconf = None,
                ):
        self.__retr_sheetname = retr_sheetname
        self.__fuction = fuction
        # Create a dict have parameter from csv 
        self.__dictconf = dict_str_from_lcsv(path=pathconf)
        # Option from user input (Active Sheet or not)
        if retr_sheetname == "Active Sheet":
            self.__ws_retr = activesheet()
        else:
            self.__ws_retr = sheet_by_namesheet(path=retr_path,
                                                namesheet=retr_sheetname)
    def ft_tool(self):
        """
        execute func of sortware \n

        ex: removespace, capfs

        """
        # filter list string only key from csv
        lfuns = filter_lstr(liststr=list(self.__dictconf.keys()),
                                        reverse_criteria=True,
                                        criteria=["sub_"],
                                        upper = False
                                        )
        # create dict have fun execute 
        mydictfun = {
                    "removespace":(lambda: self.__removespace()),
                    "capfs":(lambda: self.__capfs())
                    }
        # Option from user input function (config or not)
        if self.__fuction == "Config":
            for lfun in lfuns:
                mydictfun[lfun]()
        else:
             mydictfun[self.__fuction]()

    def __removespace(self):
        """ 
        For case function "REMOVESPACE" user select from interface 
        """

        cyesornot = self.__dictconf["removespace"]
        rmrange = self.__dictconf["sub_removespace_range"]
        rmtyle = self.__dictconf["sub_removespace_style"]
        hvalues_in_cell(rmrange=rmrange,
                        option=rmtyle,
                        ws=self.__ws_retr,
                        option_fun="removespace") if cyesornot[0] =="yes" else False        

    def __capfs(self):
        """ 
        For case function "CAPFS" user select from interface 
        """
        cyesornot = self.__dictconf["capfs"]
        rmrange = self.__dictconf["sub_capfs_range"]
        rmstype = self.__dictconf["sub_capfs_style"]
        hvalues_in_cell(rmrange=rmrange,
                        option= rmstype,
                        ws=self.__ws_retr,
                        option_fun="capfs")  if cyesornot[0] =="yes" else False