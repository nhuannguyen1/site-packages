import os
import csv
import sys

class PathSteel:

    def  __init__(self, path_Full = None,
                        dir_path = None,
                        Is_Directory_Path_To_SubFolder = False,
                        Path_Conf = None,
                        FileName = None,
                        modulename = None
                    ):
            self.path_Full = path_Full
            self.dir_path = dir_path
            #self.FolderName = FolderName
            self.Path_Conf = Path_Conf
            self.Is_Directory_Path_To_SubFolder =\
                 Is_Directory_Path_To_SubFolder
            self.FileName = FileName
            self.modulename = modulename

    # Get absolute path to resource, works for dev and for PyInstaller """
    def resource_path_is_from_pyinstall_and_dev(self):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, self.FileName)

    #function to get faname from fullpath 
    def ExtractFileNameFromPath (self):
        # get file Name
        try:
            FileName = os.path.basename(self.path_Full)
        except AttributeError as error:
            print (error)
        return FileName

    # Return full path conbine subfolder 
    def refpath(self,args = None):
        # check directory path is to subfolder or not ?
        if self.Is_Directory_Path_To_SubFolder == True:
            #unpack to get element in list
                #join 2 folder together 
            dir_path = os.path.join(self.dir_path,
                                            args)
                
                #dir_path = self.dir_path + "\\" + subFolder
            # Concatenate folder and file name 
            full_path = os.path.join(dir_path,
                                    self.FileName)
        else:
            # Create full path
            full_path = os.path.join(self.dir_path,
                                    self.FileName)
        return full_path
    # get path of module was imported 
    def getpathmodule (self):
        pathf = os.path.join((os.path.dirname(self.modulename.__file__)),
                                                self.FileName)
        return pathf

#using function to return resourse path
def resource_path_is_from_pyinstall_and_dev (FileName = None,
                                             Subfolder = None ,
                                             Is_Directory_Path_To_SubFolder = False,
                                             dir_path = None
                                            ):

    PathS = PathSteel(FileName = FileName,
                        Is_Directory_Path_To_SubFolder = Is_Directory_Path_To_SubFolder,
                        dir_path = dir_path
                    )
    return PathS.refpath(Subfolder)

#Get file name from path full
def ExtractFileNameFromPath(path = None):
       PathS = PathSteel(path_Full = path) 
       return PathS.ExtractFileNameFromPath()
 # running in a PyInstaller bundle or running in a normal Python process
def IsRunningInPyinstallerBundle ():
    try:
        if getattr(sys, 'frozen') and hasattr(sys, '_MEIPASS'):
            return True
    except:
        return False

# get Path full from directory path and file name 
def PathFromFileNameAndDirpath (dir_path = None, 
                                filename = None):
    PathS = PathSteel(dir_path = dir_path,
                        FileName = filename
                    )
    full_path = PathS.refpath()
    return full_path