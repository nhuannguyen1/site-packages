import csv
class rcsv:
    def  __init__(self, pathtor = None,
                        NumberRow = 1,
                        indexarrtoget = [0,1] ) :
        self.pathtor = pathtor
        self.NumberRow = NumberRow
        self.indexarrtoget = indexarrtoget

    # count number of row in csv 
    def CountNumberOfRow (self):
        with open(self.pathtor, 'r') as readFile:
            a = sum (1 for row in readFile)
        readFile.close
        return a

    # return all value in row by index 
    def Redtallrowbyindxaindexarr (self):
            newRowNumber = []
            with open(self.pathtor,"r") as csvFile:
                readcsv =csv.reader(csvFile, delimiter=',')
                readcsv = list(readcsv)
                RowNumber = readcsv[self.NumberRow]
                newRowNumber = [RowNumber[ind] for ind in self.indexarrtoget]
            csvFile.close()
            return newRowNumber 

    # return all value of all row 
    def Redtallrowbyindxaindexarrall (self):
        Reall = []
        recount = self.CountNumberOfRow()
        for count in range (recount):
            self.NumberRow = count
            Reall.append(self.Redtallrowbyindxaindexarr())
        return Reall

    # return all row follow index 
    def Rerowbyindxaindexarr (self):
        newRowNumber = []
        with open(self.pathtor,"r") as csvFile:
                readcsv =csv.reader(csvFile, delimiter=',')
                recount = self.CountNumberOfRow()
                for count in range (recount):
                    self.NumberRow = count
                    readcsv = list(readcsv)
                    RowNumber = readcsv[self.NumberRow]
                    #newRowNumber = [RowNumber[ind] for ind in self.indexarrtoget]
                    newRowNumber.append(RowNumber[self.indexarrtoget[0]])
        csvFile.close()
        return newRowNumber     