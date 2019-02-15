import math

def checkListInt(myList):
    try:
        for x in myList:
            int(x)
        return True
    except ValueError:
        return False

def sampleMean(myList):
    check = checkListInt(myList)
    if check == True:
        return sum(myList) / len(myList)
    else:
        return "List should contain only numbers"

def median(myList):
    check = checkListInt(myList)
    if check == True:
        myList.sort()
        length = len(myList)
        if length%2 == 0:
            return (myList[int(length / 2) - 1] + myList[int(length / 2)]) / 2
        else:
            return myList[int(length / 2)]
    else:
        return "List should contain only numbers"

def std_dev(myList):
    check = checkListInt(myList)
    if check == True:
        mean_list = sampleMean(myList)
        sd = 0
        for el in myList:
            sd += (float(el) - mean_list)**2
        sd = math.sqrt(sd / (len(myList) - 1))
        return sd
    else:
        return "List should contain only numbers"

def nQuartile(myList, n):
    if n < 1 or n > 3:
        return "Parameter should be between 1 and 3"
    else:
        check = checkListInt(myList)
        if check == True:
            myList.sort()
            if n == 1:
                length = len(myList)
                if length % 2 == 0:
                    halfVal = int(length / 2)
                else:
                    halfVal = math.ceil(length / 2) - 1
                q = median(myList[:halfVal])
            elif n == 2:
                q = median(myList)
            else:
                length = len(myList)
                if length % 2 == 0:
                    halfVal = int(length / 2)
                else:
                    halfVal = math.floor(length / 2) + 1
                q = median(myList[halfVal:])
            return q
        else:
            return "List should contain only numbers"

def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def nPercentile(myList, n):
    if n < 1 or n > 100:
        return "Parameter should be between 1 and 100"
    else:
        check = checkListInt(myList)
        if check == True:
            myList.sort()
            f = (n/100) * (len(myList))
            if f%1 == 0:
                f = int(f)
                p = (myList[f - 1] + myList[f]) / 2
            else:
                p = myList[normal_round(f) - 1]
            return p
        else:
            return "List should contain only numbers"

def decimalToRoman(n):
    try:
        n = int(n)
        if n < 1:
            return "Number needs to be a positive integer"
        roman = []
        while n >= 1000:
            roman.append('M')
            n -= 1000
        while n >= 500:
            roman.append('D')
            n -= 500
        while n >= 100:
            roman.append('C')
            n -= 100
        while n >= 50:
            roman.append('L')
            n -= 50
        while n >= 10:
            roman.append('X')
            n -= 10
        while n >= 5:
            roman.append('V')
            n -= 5
        while n >= 1:
            roman.append('I')
            n -= 1
        romanString = ''.join(roman)
        return romanString
    except ValueError:
        return "Number needs to be a integer"