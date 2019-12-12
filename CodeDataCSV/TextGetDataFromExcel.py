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

from pynvn.excel import toexcel
# check running in Pyintaller or not ?


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
                "LocationOfPurlin",
                "startrow",
                ]
                
    #location in conf
    locvalue = [12,16,17,19,20,21,23,24,25,26,30]

    credict_c = credict(KeyValues = keyvalue, 
                        LocConf = locvalue,
                        Config_Setting_Path = fullpath)
    credict_list = credict_c.Dictfromkeyandvalueconf()

    # create arr from keyvalue  
    valgen = credict_list.get("ValueGeneral", "")

    valgen = [int(i) for i in credict_list.get("ValueGeneral", "")]

    colmv = credict_list.get("Columnmove", "")
    locmvcol = credict_list.get("LocationCellForMoveColumn", "")
    gencolnotchg = credict_list.get("GenneralColumnNotChange", "")
    genconraf = credict_list.get("GeneralConcernRaffter", "")
    gensel = credict_list.get("Genneral_Select", "")
    locrowleft = credict_list.get("LocationOfRowLeft", "")
    locrowright = credict_list.get("LocationOfRowRight", "")
    excemvcolright = credict_list.get("ExcelCellForMoveColumnRight", "")
    locpur = credict_list.get("LocationOfPurlin", "")
    strow = credict_list.get("startrow", "")

    # data template  
    if IsRunningInPyinstallerBundle():
        #NameFile = ExtractFileNameFromPath(DataExcel)
        DataExcel = resource_path_is_from_pyinstall_and_dev(FileName = 'DataALL - Template.xlsx',
                                                         Subfolder="Data",
                                                         Is_Directory_Path_To_SubFolder= True,
                                                         dir_path=sys._MEIPASS)
    else:
        DataExcel = 'DataALL - Template.xlsx'


    book = load_workbook(DataExcel)
    writer = ExcelWriter(DataExcel,
                        engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

    for path in [Left_Genneral_All_path,
                Right_Genneral_All_path]:
            
            df1 = pd.read_csv(path, delimiter=',',
                                    index_col = 0)
            dfCount = df1.shape
            df1.to_csv(path)
            #write Left to Excel 
            dfValueGeneral = pd.read_csv(path, 
                                        delimiter=',',
                                        usecols  = valgen,
                                        nrows= 1)

            dfValueGeneral.to_excel(writer,'General Member',
                                    index=False,header=True ,
                                    startcol=0,startrow \
                                    = strow[0])

            worksheet = writer.sheets['General Member']

            # create frame to excel 
            excellframe = toexcel(worksheet = worksheet,
                                            path = path,
                                            path_conf =fullpath,
                                            lpath=Left_Genneral_All_path,
                                            rpath = Right_Genneral_All_path)

            if path == Left_Genneral_All_path:
                usecolsArr = locrowleft
                LocationMoveColumn = locmvcol
                #write path to excel 
                excellframe.wrivaltoexc()
            else:
                usecolsArr = locrowright
                LocationMoveColumn = excemvcolright
                #write path to excel 
                excellframe.wrivaltoexc()
            #Write genneral to excel
            DfChangegenneral = pd.read_csv(path,
                                         delimiter=',',
                                         usecols = gencolnotchg,
                                         nrows= 1 
                                         )

            DfChangegenneral.to_excel(writer,
                                    'General Member',
                                    index=False,
                                    header=True,
                                    startcol=0,
                                    startrow= int(usecolsArr[1])
                                    )

            #write Genneral Concern Raffter
            DfChangegenneral = pd.read_csv(path,
                                             delimiter=',',
                                             usecols = genconraf 
                                             )

            DfChangegenneral.to_excel(writer,
                                    'General Member',
                                    index=False,
                                    header=True ,
                                    startcol=0,
                                    startrow=int(usecolsArr[2])
                                    )

            #write genneral selected 
            DfChangegenneral = pd.read_csv(path,
                                     delimiter=',',
                                     usecols = gensel,
                                     nrows= 1)
            DfChangegenneral.to_excel(writer,
                                    'General Member',
                                    index=False,
                                    header=True ,
                                    startcol=0,
                                    startrow= int(usecolsArr[0])
                                    )

            #write purlin roof 
            DfChangegenneral = pd.read_csv(path,
                                         delimiter=',',
                                         usecols = locpur,
                                         nrows= 1)

            DfChangegenneral.to_excel(writer,
                                    'General Member',
                                    index=False,
                                    header=True ,
                                    startcol=0,
                                    startrow= int(usecolsArr[3]))
            worksheet = writer.sheets['General Member']

            #Wirte move Column to excel
            excellframe.writemovecol(LocationMoveColumn,
                                                colmv)
    book.save('new_big_file.xlsx') 
