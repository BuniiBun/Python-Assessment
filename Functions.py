#Imports
import csv

#Functions
def CSVtoDict(PathToCSV):
    with open(PathToCSV) as CSVFile:
        CSVReader = csv.reader(CSVFile, delimiter = ",")
        LineCount = 0
        DictName = PathToCSV[:-4]
        Dictionary = {}
        Dictionary[DictName] = []
        Elements = []
        for Row in CSVReader:
            if LineCount == 0:
                for Element in Row:
                    Elements.append(Element)
                LineCount += 1
            else:
                ElementDict = {}
                LoopCount = 0
                for Element in Elements:
                    # - Bit of hardcoding the function so we get an int student id instead of a string
                    if Element == "id":
                        ElementDict[Element] = int(Row[LoopCount])
                    #
                    else:
                        ElementDict[Element] = Row[LoopCount]
                    LoopCount += 1
                Dictionary[DictName].append(ElementDict)
                LineCount += 1
        return Dictionary

def CalculateAvg(List):
    Sum = 0
    for Number in List:
        Sum = Sum + int(Number)

    Avg = Sum / len(List)
    return Avg