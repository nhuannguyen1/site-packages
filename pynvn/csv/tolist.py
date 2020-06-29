import csv
def convertcsvtolist(path):
    """ convert csv to list """
    with open(path, newline='') as inputfile:
        results = [row[0] for row in csv.reader(inputfile)]
    return results