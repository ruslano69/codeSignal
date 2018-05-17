def allLongestStrings(inputArray):
    longestStr = len(inputArray[0])
    for index in range(1,len(inputArray)):
        if longestStr < len(inputArray[index]):
            longestStr = len(inputArray[index])
    return [x for x in inputArray if len(x) == longestStr]
