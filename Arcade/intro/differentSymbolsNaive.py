def differentSymbolsNaive(s):
    counter = 0
    found = []
    
    for char in s:
        if char not in found:
            counter += 1
            found.append(char)
    return counter
