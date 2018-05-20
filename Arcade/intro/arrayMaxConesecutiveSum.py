def arrayMaxConsecutiveSum(inputArray, k):
    inputSum = 0
    maxS = 0
    
    for i in range(k):
        inputSum += inputArray[i]
    
    maxS = inputSum
    
    for j in range(k, len(inputArray)):
        inputSum -= inputArray[j-k]
        inputSum += inputArray[j]
        if inputSum > maxS:
            maxS = inputSum
    return maxS