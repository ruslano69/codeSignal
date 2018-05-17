def isLucky(n):
    return sum([int(x) for x in list(str(n)[:len(str(n))//2])]) == sum([int(x) for x in list(str(n)[len(str(n))//2:])])