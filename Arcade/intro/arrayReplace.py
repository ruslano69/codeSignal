def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for element in range(len(inputArray)):
        if inputArray[element] == elemToReplace:
            inputArray[element] = substitutionElem
    return inputArray
