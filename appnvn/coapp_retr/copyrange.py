from pynvn.excel.copy_move_paste import co_paste_move_range
from pynvn.excel import listsheet_by_wb
from pynvn.check.list import check_list_value
def hsheet_range(sheet_name, 
                wb,
                range_copy,
                range_paste,
                clear_rcopy_after_copy = True, 
                usinglocinexcel = False
                ):
    """ copy move paste range """
    # this case for active 
    if sheet_name == "active":
        ws = wb.sheets.active
        if usinglocinexcel:
            range_copy = ws.range(range_copy).value
            range_paste = ws.range(range_paste).value
            co_paste_move_range(sheet_copy= ws,
                                    sheet_des= ws,
                                    range_copy=range_copy,
                                    range_paste=range_paste,
                                    clear_rcopy_after_copy=clear_rcopy_after_copy
                                    ) 

        else:
            co_paste_move_range(sheet_copy= ws,
                                    sheet_des= ws,
                                    range_copy=range_copy,
                                    range_paste=range_paste,
                                    clear_rcopy_after_copy=clear_rcopy_after_copy
                                    )

    else:
        for sheetname in listsheet_by_wb(wb):
            if sheet_name in sheetname:
                wb.sheets[sheetname].activate()
                ws = wb.sheets.active
                if usinglocinexcel: 
                    range_copy = ws.range(range_copy).value
                    range_paste = ws.range(range_paste).value
                    co_paste_move_range(sheet_copy=ws,
                                        range_copy=range_copy,
                                        sheet_des=ws,
                                        range_paste=range_paste,
                                        clear_rcopy_after_copy=clear_rcopy_after_copy
                                        )
                else:
                    co_paste_move_range(sheet_copy=ws,
                                        range_copy=range_copy,
                                        sheet_des=ws,
                                        range_paste=range_paste,
                                        clear_rcopy_after_copy=clear_rcopy_after_copy
                                        )

class cpfromtem:
    """ copy move paste range """
    def __init__(self,
                ws_des = None,
                ws_tem = None,
                range_copy = "",
                range_paste = "",
                clear_rcopy_after_copy = True, 
                usinglocinexcel = False,
                ):
        self.ws_des = ws_des
        self.ws_tem = ws_tem
        self.range_copy = range_copy
        self.range_paste = range_paste
        self.clear_rcopy_after_copy = clear_rcopy_after_copy
        self.usinglocinexcel = usinglocinexcel
        self.__hfun()

    def __hfun(self):
        self.__cp_using_loc(sheet_copy=self.ws_tem,
                                sheet_des=self.ws_des) if self.usinglocinexcel else self.__not_cp_using_loc(sheet_copy=ws_tem,
                                                                                                    sheet_des=self.ws_des)
    def __cp_using_loc(self,
                        sheet_copy,
                        sheet_des
                        ):
        co_paste_move_range(sheet_copy= sheet_copy,
                            sheet_des= sheet_des,
                            range_copy=range_copy,
                            range_paste=range_paste,
                            clear_rcopy_after_copy=self.clear_rcopy_after_copy,
                            usinglocinexcel=True
                            )
            
    def __not_cp_using_loc(self,
                            sheet_copy,
                            sheet_des
                            ):
        co_paste_move_range(sheet_copy= sheet_copy,
                            sheet_des= sheet_des,
                            range_copy=range_copy,
                            range_paste=range_paste,
                            clear_rcopy_after_copy=clear_rcopy_after_copy,
                            usinglocinexcel=False
                            )
