def makeArrayConsecutive2(statues):
    counter = 0 # initialize counter
    statues.sort()
    for statue in range(1,len(statues)):
        
        if statues[statue - 1] + 1 != statues[statue]:
            statuesR = statues[statue-1]
            while True:
                statuesR += 1
                if statuesR == statues[statue]:
                    break
                else:
                    counter +=1 
    return counter