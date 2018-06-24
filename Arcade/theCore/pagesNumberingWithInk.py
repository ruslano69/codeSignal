def pagesNumberingWithInk(current, numberOfDigits):
    while True:
        numberOfDigits -= len(str(current))
        if numberOfDigits < len(str(current + 1)):
            break
        current += 1
        
        
    return current
