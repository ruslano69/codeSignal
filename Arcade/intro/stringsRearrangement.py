from itertools import permutations

def stringsRearrangement(inputArray):
    possiblePermutations = permutations(inputArray)
    
    for perms in possiblePermutations:
        allMatch = True
        for i in range(len(perms) - 1):
            if not isDifferByOneChar(perms[i], perms[i+1]):
                allMatch = False
                break
        if allMatch:
            return True
    return False

def isDifferByOneChar(str1, str2):
    counter = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            counter += 1
    return counter == 1
