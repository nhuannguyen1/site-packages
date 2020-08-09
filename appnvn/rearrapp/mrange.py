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
    if sheet_name == "active":
        if usinglocinexcel:
            ws = wb.sheets.active
            range_copy = ws.range(range_copy).value
            range_paste = ws.range(range_paste).value
            if check_list_value(valuetocheck=[range_copy,range_paste]):
                co_paste_move_range(sheet_copy= ws,
                                    sheet_des= ws,
                                    range_copy=range_copy,
                                    range_paste=range_paste,
                                    clear_rcopy_after_copy=clear_rcopy_after_copy
                                    ) 

        else:
            if check_list_value(valuetocheck=[range_copy,range_paste]):
                ws = wb.sheets.active
                co_paste_move_range(sheet_copy= ws,
                                    sheet_des= ws,
                                    range_copy=range_copy,
                                    range_paste=range_paste,
                                    clear_rcopy_after_copy=clear_rcopy_after_copy
                                    )

    else:
        for sheetname in listsheet_by_wb(wb):
            if sheet_name in sheetname:
                if usinglocinexcel: 
                    wb.sheets[sheetname].activate()
                    ws = wb.sheets.active
                    range_copy = ws.range(range_copy).value
                    range_paste = ws.range(range_paste).value
                    if check_list_value(valuetocheck=[range_copy,range_paste]):
                        co_paste_move_range(sheet_copy=ws,
                                            range_copy=range_copy,
                                            sheet_des=ws,
                                            range_paste=range_paste,
                                            clear_rcopy_after_copy=clear_rcopy_after_copy
                                            )
                else:
                    wb.sheets[sheetname].activate()
                    ws = wb.sheets.active
                    if check_list_value(valuetocheck=[range_copy,range_paste]):
                        co_paste_move_range(sheet_copy=ws,
                                            range_copy=range_copy,
                                            sheet_des=ws,
                                            range_paste=range_paste,
                                            clear_rcopy_after_copy=clear_rcopy_after_copy
                                            )