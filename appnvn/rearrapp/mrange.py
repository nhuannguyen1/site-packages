from pynvn.excel.copy_move_paste import co_paste_move_range
def hsheet_range(sheet_name, wb,range_copy,range_paste,clear_rcopy_after_copy = True):
    """ copy move paste range """
    if sheet_name == "active":
        ac_sheet = wb.sheets.active
        co_paste_move_range(sheet_copy=ac_sheet,
                        sheet_des=ac_sheet,
                        range_copy=range_copy,
                        range_paste=range_paste,
                        clear_rcopy_after_copy=clear_rcopy_after_copy
                        )
    else:
        for sheetname in listsheet_by_wb(wb):
            if sheet_name in sheetname:
                wsheet = wb.sheets[sheetname]
                co_paste_move_range(sheet_copy=wsheet,
                                range_copy=range_copy,
                                sheet_des=wsheet,
                                range_paste=range_paste,
                                clear_rcopy_after_copy=clear_rcopy_after_copy
                                )