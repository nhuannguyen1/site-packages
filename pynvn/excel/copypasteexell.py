import xlwings as xw
def cprange(pathtocopy,rangetocopy='BB5:CF100' ,rangetopaste="BB5", namesheettocopy ='sheet_config' ):

    """ copy and paste range excel to another file
        ex: copy range [A1:C3] of pathtocopy to 
        C5:E20 of pathtodes
        copy to active sheet
    """
    # visible excel file
    app = xw.App(visible=False)
    sheetdesactive = xw.sheets.active
    print (sheetdesactive)
    wbtocopy = xw.Book(pathtocopy)
    sheet_copy = wbtocopy.sheets[namesheettocopy]
    print (sheet_copy)
    sheet_copy.range(rangetocopy).api.copy
    sheetdesactive.range(rangetopaste).api.select
    sheetdesactive.api.paste
    # not cut excel 
    wbtocopy.app.api.CutCopyMode=False
    wbtocopy.close()
    app.quit()
cprange(pathtocopy =r"D:\0.Good Drive - sn\AZBSW\config\config_hm.xlsx")
