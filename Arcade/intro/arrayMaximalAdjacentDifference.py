def arrayMaximalAdjacentDifference(inputArray):
    diffArray = []
    for index in range(1,len(inputArray)):
        diffArray.append(abs(inputArray[index]-inputArray[index-1]))
    return max(diffArray)
