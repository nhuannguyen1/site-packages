import csv
class SaveDataToCSV:
    def  __init__(self, path):
        self.path = path
    def SaveDataH_tAndH_N(self,H_n,H_t):
        lines = [["H_n","H_t"],[H_n,H_t]]
        with open(self.path, 'w') as csvFile:
            writer = csv.writer(csvFile,lineterminator='\n')
            writer.writerows(lines)
        csvFile.close()