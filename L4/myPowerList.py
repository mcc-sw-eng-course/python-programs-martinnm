##Martin Francisco Noriega Moreno
##Development Exercises - L2

from pathlib import Path

class myPowerList:
    def __init__(self):
        self.list = list()

    def readFromTextFile(self, filename):
        filePath = Path(filename)
        if filePath.suffix == '.txt':
            file = open(filename, 'r')
            return file.read()
            file.close()
        else:
            return "Invalid file name"

