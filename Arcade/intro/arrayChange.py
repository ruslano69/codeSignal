def arrayChange(inputArray):
    counter = 0
    for i in range(1, len(inputArray)):
        if inputArray[i-1] >= inputArray[i]:
            diff = (inputArray[i-1] + 1) - inputArray[i]
            inputArray[i] = inputArray[i-1] + 1
            counter += diff
    return counter
