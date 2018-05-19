def avoidObstacles(inputArray):
    
    inputArray.sort()

    maxVal = inputArray[-1]
    for index in range(1, maxVal + 2):
        if all(item % index != 0 for item in inputArray):
            return index