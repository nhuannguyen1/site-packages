import xlwings as xw
def cprange(pathtocopy = None,rangetocopy='BB5:CF100',pathtodes = None,rangetopaste="BB5", namesheettocopy ='sheet_config' ):

    """ copy and paste range excel to another file
        ex: copy range [A1:C3] of pathtocopy to 
        C5:E20 of pathtodes
        copy to active sheet
    """
    # visible excel file
    #app = xw.App(visible=False)
    #sheetdesactive = xw.sheets.active
    pathtodes.range(rangetopaste).api.select
    wbtocopy = xw.Book(pathtocopy)
    sheet_copy = wbtocopy.sheets[namesheettocopy]
    sheet_copy.range(rangetocopy).api.copy
    pathtodes.api.paste
    # not cut excel 
    wbtocopy.app.api.CutCopyMode=False
    wbtocopy.close()
    #app.quit()
#cprange(pathtocopy =r"D:\0.Good Drive - sn\AZBSW\config\config_hm.xlsx")
