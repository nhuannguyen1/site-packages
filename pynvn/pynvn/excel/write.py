from pynvn.excel.list import lnumbercolumnbyrangstr
from pynvn.stringnvn.slist import returnseplistintbbystr
from pynvn.excel.del_row import delrowbyrange
from pynvn.excel.rows import startrow_endrow

class del_row(object):
    """ 
    handling range for sheet\n
    rmrange: Range to handling string: \n
    ex: A1, A1:B3,A
    ws: worksheet corresponds to the rmrange \n
    option: style to  handling:\n
    ex: tspacetoospace, fs,upper_all,both, left, right,lower_all,all \n
    option_fun: For case function "REMOVESPACE or CAPFS" user select from interface \n
    ex: REMOVESPACE,CAPFS
    """
    def __init__(self,f):
        self.f = f
    def __call__(self, **kwargs):
        self.__ws = kwargs["ws"]
        rmrange = kwargs["rmrange"]
        self.valuetodelete = kwargs["valuetodelete"]
        self.using_value_to_end = kwargs.get("using_value_to_end",False)
        self.value_to_end = kwargs.get("value_to_end","")
        for rangea in rmrange:
            self.__cols=lnumbercolumnbyrangstr(rstr=rangea)
            self.__rows=returnseplistintbbystr(strint=rangea)
            self.del_fun()

    def del_fun(self):

        a,b = startrow_endrow(ws=self.__ws,
                              rows=self.__rows,
                              cols=self.__cols
                              )
        for col in self.__cols:
            self.f(incolumndel=col,
                   ws=self.__ws,
                   startrow=a,
                   endrow=b,
                   using_value_to_end=self.using_value_to_end,
                   valuetodelete=self.valuetodelete,
                   value_to_end= self.value_to_end
                   )