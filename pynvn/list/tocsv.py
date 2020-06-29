import csv
def listocsvhor(pathtow = None,listv = None):
    """ convert list to csv horizontal """
    with open(pathtow, 'w') as csvFile:
        wr = csv.writer(csvFile,lineterminator='\n')
        wr.writerow(listv)
    csvFile.close()

def listocsvver(pathtow = None,listv = None):
    """ convert list to csv vertival """
    with open(pathtow, "w") as f:
        writer = csv.writer(f,lineterminator='\n')
        for row in listv:
            writer.writerow([row])