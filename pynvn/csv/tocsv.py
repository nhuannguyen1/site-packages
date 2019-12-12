import csv
class wrcsv:
    def  __init__(self, pathtow = None,*args,**kwargs):
        self.pathtow = pathtow
        self.args = args
        self.kwargs = kwargs

    def savevaltocsv(self):
        with open(self.pathtow, 'w') as csvFile:
            writer = csv.writer(csvFile,delimiter =',',lineterminator='\n')
            writer.writerows(self.args)
        csvFile.close()
    def ReDtallrowbyIndx (self,NumberRow):
            with open(self.pathtow,"r") as csvFile:
                readcsv =csv.reader(csvFile, delimiter=',')
                readcsv = list(readcsv)
                RowNumber = readcsv[NumberRow]
            csvFile.close()
            return RowNumber