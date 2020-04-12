from pynvn.path.ppath import PathSteel
from appnvn.exazp.hdata import hdata
class kidtomother:
    def __init__(self,pathfolder = None,
                fileparent = "WHITEX - TONG HOP NGAN SACH.xlsx",
                filekid = "AZB-INPUT.xlsx",
                subfolderinput = "0.input",
                subfolderoutput = "1.output"
                ):
                self.fileparent = fileparent
                self.pathfolder = pathfolder
                self.filekid = filekid
                self.subfolderinput = subfolderinput
                self.subfolderoutput = subfolderoutput

                self.ps = PathSteel(dir_path=self.pathfolder,
                                    Is_Directory_Path_To_SubFolder=True,
                                    subfolder=self.subfolderinput,
                                    FileName=self.filekid)
                # return file kid 
                self.pathkid =  self.ps.refpath()
                # return fileparent 
                self.ps.subfolder = self.subfolderoutput
                self.ps.FileName = self.fileparent
                self.pathparent = self.ps.refpath

    def hldatakid(self):
        hdata(pathfile=self.pathkid).hldatakid()
        
