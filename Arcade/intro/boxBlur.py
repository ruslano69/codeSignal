from math import floor
def boxBlur(image):
    outputArray = []
    
    for y in range(len(image) - 2):
        line = []
        for x in range( len(image[y]) - 2):
            Isum = 0
            counter = 0
            for a in range(y, y + 3):
                for b in range(x, x+3):
                    Isum += image[a][b]
                    counter += 1
            line.append(floor(Isum/counter))
        outputArray.append(line)
    return outputArray