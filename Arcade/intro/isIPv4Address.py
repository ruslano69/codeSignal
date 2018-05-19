def isIPv4Address(inputString):
    numArray = inputString.split('.')
    if len(numArray) < 4 or len(numArray) > 4 or '' in numArray:
        return False
    for num in numArray:
        if  num.isupper() or num.islower():
            return False
        if int(num) > 255 or int(num) < 0:
            return False
    return True