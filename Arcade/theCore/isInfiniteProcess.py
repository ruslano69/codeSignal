def isInfiniteProcess(a, b):
    if a == b:
        return False
    elif a > b:
        return True
    else:
        return (b-a)%2 != 0
            