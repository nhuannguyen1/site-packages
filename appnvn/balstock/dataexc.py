from tkinter.constants import NONE
import pandas as pd
from pathlib import Path
from pynvn.path.ppath import ExtractFileNameFromPath
from pynvn.csv.tocsv import wrcsv
import sys

class comparetwofile():
    def __init__(self,path_OLD = None, 
                path_NEW = None, 
                index_col = None,
                sheetname = 0,
                usernamein = None,
                dt = None
                ) :
        self.path_OLD = path_OLD
        self.path_NEW = path_NEW
        self.index_col = index_col
        self.sheetname = sheetname
        self.usernamein = usernamein
        self.dt = dt
    def excel_diff(self):
        # get sheet name file 
        xl = pd.ExcelFile(self.path_OLD)

        shname =  xl.sheet_names[0]  # see all sheet names


        df_OLD = pd.read_excel(self.path_OLD,sheet_name=self.sheetname,
                                index_col=self.index_col).fillna("")
        df_NEW = pd.read_excel(self.path_NEW,sheet_name=self.sheetname, 
                                index_col=self.index_col).fillna("")
        filename = ExtractFileNameFromPath(self.path_NEW)
        # Perform Diff
        dfDiff = df_NEW.copy()
        droppedRows = []
        newRows = []
        diffRows = []
        rowandcolumn = []
        indexoldnew = []
        cols_OLD = df_OLD.columns
        cols_NEW = df_NEW.columns
        sharedCols = list(set(cols_OLD).intersection(cols_NEW))
        for row in dfDiff.index:
            if (row in df_OLD.index) and (row in df_NEW.index):
                for col in sharedCols:
                    value_OLD = df_OLD.loc[row,col]
                    value_NEW = df_NEW.loc[row,col]
                    if value_OLD==value_NEW:
                        dfDiff.loc[row,col] = df_NEW.loc[row,col]
                    else:
                        dfDiff.loc[row,col] = ('{}→{}').format(value_OLD,
                                                                value_NEW)

                        df_NEW.loc[row,100] = ('{} changed data to {} at {}').format(self.usernamein,
                                                                                value_NEW,self.dt)
                        # get index column
                        col_index = df_NEW.columns.get_loc(col)

                        rowandcolumn.append([row + 1,
                                            col_index])

                        indexoldnew.append([row + 1,col_index,value_OLD,value_NEW])

                        diffRows.append(row)
            else:
                newRows.append(row)
        # save as to csv file 
        datachange = [[self.usernamein,self.dt,indexoldnew]]
        #wcsv1 = wrcsv (pathtow = r"C:\Users\nhuan.nguyen\Desktop\Original\test 2\nhuan.csv",list =datachange)
        df = pd.DataFrame(data=datachange)
        df.to_csv (r"C:\Users\nhuan.nguyen\Desktop\Original\test 2\npandas.csv",
                    index = None,
                    header=False, 
                    mode = "a")    
        #wcsv1.writefilecsvFromRowArr()        
        for row in df_OLD.index:
            if row not in df_NEW.index:
                droppedRows.append(row)
                dfDiff = dfDiff.append(df_OLD.loc[row,:])

        dfDiff = dfDiff.sort_index().fillna('')
        # Save output and format
        #fname = "Test12.xlsx"
        fname = '{}_Change.xlsx'.format(filename)
        
        writer = pd.ExcelWriter(self.path_OLD, 
                                engine='xlsxwriter')

        #cteate file new excel 
        df_NEW.to_excel(writer, sheet_name=shname, 
                                index=False)
        
        #compare 2 file 
        dfDiff.to_excel(writer, sheet_name='DIFF', 
                                index=False)

        #df_OLD.to_excel(writer, sheet_name=path_OLD.stem, index=False)

        diffRows = list(set(diffRows+newRows+droppedRows))
        df_Changes = dfDiff.loc[diffRows,:]

        # get xlsxwriter objects
        workbook  = writer.book
        worksheet = writer.sheets['DIFF']
        worksheet_org = writer.sheets[shname]
        worksheet.hide_gridlines(2)
        worksheet.set_default_row(15)

        # define formats
        date_fmt = workbook.add_format({'align': 'center', 'num_format': 'yyyy-mm-dd'})
        center_fmt = workbook.add_format({'align': 'center'})
        number_fmt = workbook.add_format({'align': 'center', 'num_format': '#,##0.00'})
        cur_fmt = workbook.add_format({'align': 'center', 'num_format': '$#,##0.00'})
        perc_fmt = workbook.add_format({'align': 'center', 'num_format': '0%'})
        grey_fmt = workbook.add_format({'font_color': '#E0E0E0'})
        highlight_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color':'#B1B3B3'})
        new_fmt = workbook.add_format({'bg_color': '#C6EFCE','font_color': '#32CD32','bold':True})

        
        # set format over range
        ## highlight changed cells
        worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value':'→',
                                                'format': highlight_fmt})
        

        for cell in rowandcolumn:

            worksheet_org.conditional_format(int(cell[0]),int(cell[1]),int(cell[0]),int(cell[1]), {'type': 'no_errors',
                                          'format': new_fmt})

        worksheet_org.conditional_format('A1:ZZ1000', {'type': 'text',
                                                'criteria': 'containing',
                                                'value':'changed data to',
                                                'format': new_fmt})
                                    
        # highlight new/changed rows
        for row in range(dfDiff.shape[0]):
            if row+1 in newRows:
                worksheet.set_row(row+1, 15, new_fmt)
            if row+1 in droppedRows:
                worksheet.set_row(row+1, 15, grey_fmt)
        # save
        writer.save()