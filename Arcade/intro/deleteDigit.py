def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def deleteDigit(n):
    numStr = str(n)
    currentMax = 0
    for digit in range(len(numStr)):
        newNum = int(replace_str_index(numStr,digit))
        if newNum > currentMax:
            currentMax = newNum
    return currentMax
        
