import csv
class wrcsv:
    def  __init__(self, pathtow = None,list = None,**kwargs):
        self.pathtow = pathtow
        self.args = list
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
    def writefilecsvFromRowArr(self):
        with open(self.pathtow , 'a') as csvFile:
            writer = csv.writer(csvFile,lineterminator='\n')
            writer.writerow(self.args)
        csvFile.close()