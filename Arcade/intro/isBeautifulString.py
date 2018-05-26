def isBeautifulString(inputString):
    for char in inputString:
        if char == "a":
            continue
        count01 = inputString.count(char)
        count02 = inputString.count(chr(ord(char) - 1)) if char != "z" else inputString.count("y")
        if count01 > count02:
            return False
    return True