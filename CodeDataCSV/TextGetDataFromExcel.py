import os
import sys
import pandas as pd
from pandas import ExcelWriter,ExcelFile
import numpy as np
import openpyxl
from openpyxl import load_workbook

from pynvn.path import (IsRunningInPyinstallerBundle,
                        resource_path_is_from_pyinstall_and_dev,
                        ExtractFileNameFromPath,
                        PathFromFileNameAndDirpath,
                        )

from pynvn.dict import credict
"""
from Csv_Excel import (AligntText,
                        ValueGeneral,
                        Columnmove,
                        LocationCellForMoveColumn,
                        GenneralColumnNotChange,
                        GeneralConcernRaffter,
                        Genneral_Select,
                        LocationOfRowLeft,
                        LocationOfRowRight,
                        ExcelCellForMoveColumnRight,
                        LocationOfPurlin,
                        WriteMoveColumn,
                        Write_Path_ToExcel,
                        startrow)
"""
"""
from Path_Connect_Excel import (Right_Genneral_All_path,
                                Left_Genneral_All_path,
                                DataExcel)
"""

# check running in Pyintaller or not ?
if IsRunningInPyinstallerBundle():
    #NameFile = ExtractFileNameFromPath(DataExcel)
    DataExcel = resource_path_is_from_pyinstall_and_dev(FileName = 'DataALL - Template.xlsx',
                                                         Subfolder="Data",
                                                         Is_Directory_Path_To_SubFolder= True,
                                                         dir_path=sys._MEIPASS)

def CreateFileExcel(paths):
    filename = "Config_Setting.csv"
    fullpath = os.path.join(paths,filename)

    # get path store data to handling
    Right_Genneral_All_path = PathFromFileNameAndDirpath(dir_path =paths,
                                                         filename ="Right_Genneral_All.csv"
                                                         )
                                    
    Left_Genneral_All_path = PathFromFileNameAndDirpath(dir_path =paths,
                                                         filename ="Left_Genneral_All.csv"
                                                         )

    # key value 
    keyvalue = ["ValueGeneral",
                "Columnmove",
                "LocationCellForMoveColumn",
                "GenneralColumnNotChange",
                "GeneralConcernRaffter",
                "Genneral_Select",
                "LocationOfRowLeft",
                "LocationOfRowRight",
                "ExcelCellForMoveColumnRight",
                "LocationOfPurlin"]
    #location in conf
    locvalue = [12,16,17,19,20,21,23,24,25,26]

    credict_c = credict(KeyValues = keyvalue, LocConf = locvalue, Config_Setting_Path = fullpath)
    valuelist = credict_c.getvaluefromconfigpath()
    print ("valuelist",valuelist)






    book = load_workbook('DataALL - Template.xlsx')
    writer = ExcelWriter('DataALL - Template.xlsx',engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    #ArrMaxValue = IndexGeneral + Columnmove + IndexChange
    for path in [Left_Genneral_All_path,Right_Genneral_All_path]:
            df1 = pd.read_csv(path, delimiter=',',index_col = 0)
            dfCount = df1.shape
            df1.to_csv(path)
            #write Left to Excel 
            dfValueGeneral = pd.read_csv(path, 
                                        delimiter=',',
                                        usecols = ValueGeneral,
                                        nrows= 1)
            dfValueGeneral.to_excel(writer,'General Member',
                                    index=False,header=True ,
                                    startcol=0,startrow= int(startrow[0]))
            worksheet = writer.sheets['General Member']
            if path == Left_Genneral_All_path:
                usecolsArr = LocationOfRowLeft
                LocationMoveColumn = LocationCellForMoveColumn
                #write path to excel 
                Write_Path_ToExcel(worksheet,path)
            else:
                usecolsArr = LocationOfRowRight
                LocationMoveColumn = ExcelCellForMoveColumnRight
                #write path to excel 
                Write_Path_ToExcel(worksheet,path)
            #Write genneral to excel
            DfChangegenneral = pd.read_csv(path, delimiter=',',usecols = GenneralColumnNotChange,nrows= 1 )
            DfChangegenneral.to_excel(writer,'General Member',index=False,header=True ,startcol=0,startrow= int(usecolsArr[1]) )
            #write Genneral Concern Raffter
            DfChangegenneral = pd.read_csv(path, delimiter=',',usecols = GeneralConcernRaffter )
            DfChangegenneral.to_excel(writer,'General Member',index=False,header=True ,startcol=0,startrow=int(usecolsArr[2]))
            #write genneral selected 
            DfChangegenneral = pd.read_csv(path, delimiter=',',usecols = Genneral_Select,nrows= 1)
            DfChangegenneral.to_excel(writer,'General Member',index=False,header=True ,startcol=0,startrow= int(usecolsArr[0]))
            #write purlin roof 
            DfChangegenneral = pd.read_csv(path, delimiter=',',usecols = LocationOfPurlin,nrows= 1)
            DfChangegenneral.to_excel(writer,'General Member',index=False,header=True ,startcol=0,startrow= int(usecolsArr[3]))
            worksheet = writer.sheets['General Member']
            #Wirte move Column to csv
            WriteMoveColumn(pd,worksheet,path,LocationMoveColumn,Columnmove)
            # align text for worksheet 
            AligntText(worksheet)
    book.save('new_big_file.xlsx') 
CreateFileExcel(r"C:\Users\nhuan.nguyen\AppData\Roaming\pyRevit\Extensions\PySteelFraming.extension\PySteelFraming.tab\GetDataFromColumnAndFraming.panel\TestDataToExcel.pushbutton\Data_CSV")