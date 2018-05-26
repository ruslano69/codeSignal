def isMAC48Address(inputString):
    if inputString[-1] == "-" or len(inputString) != 17:
        return False
    inputList = inputString.split('-')
    validChars = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
    for st in inputList:
        for char in list(st):
            if char not in validChars:
                return False
    return True
