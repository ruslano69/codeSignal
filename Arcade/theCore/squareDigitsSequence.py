def squareDigitsSequence(a0):
    counter = 0
    sequence = [a0]
    
    while True:
        an = sequence[counter]
        anS = str(an)
        new_an = 0
        for num in range(len(anS)):
            new_an += int(anS[num])**2
        
        if new_an in sequence:
            counter += 1
            break
        else:
            sequence.append(new_an)
            counter += 1
    return counter + 1
