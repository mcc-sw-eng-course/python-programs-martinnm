##Martin Francisco Noriega Moreno
##Development Exercises - L2

from pathlib import Path

class directoryOfUsers:
    def __init__(self):
        self.records = dict()
        self.key = 0

    def newRecord(self, name, address, phone, email):
        self.key += 1
        key = str(self.key)
        self.records[key] = dict()
        self.records[key]['name'] = name
        self.records[key]['address'] = address
        self.records[key]['phone'] = phone
        self.records[key]['email'] = email

    def saveAllRecords(self, file):
        filePath = Path(file)
        if filePath.suffix == '.txt':
            output = open(file, 'w')
            for element in self.records:
                output.write(str(self.records[element]['name']) + "~")
                output.write(str(self.records[element]['address']) + "~")
                output.write(str(self.records[element]['phone']) + "~")
                output.write(str(self.records[element]['email']))
                output.write("\n")
            output.close()
        else:
            return "Incorrect file name."


    def loadRecords(self, file):
        filePath = Path(file)
        input = open(filePath, 'r')
        for element in input:
            values = element.split("~")
            self.newRecord(values[0], values[1], values[2], values[3])
        input.close()


    def searchData(self, data):
        if(data in self.records):
            return self.records[data]
        else:
            return "Data not found"