def additionWithoutCarrying(param1, param2):
    param1S, param2S = str(param1), str(param2)
    
    if len(param1S) >= len(param2S):
        longer = param1S[::-1]
        shorter = param2S[::-1]
    else:
        shorter = param1S[::-1]
        longer = param2S[::-1]
    result = ""
    counter = 0
    
    for char in longer:
        if counter >= len(shorter):
            result += char
        else:
            num = int(char) + int(shorter[counter])
            counter += 1
            
            if num > 9:
                result += str(num -10)
            else:
                result += str(num)
    return int(result[::-1])