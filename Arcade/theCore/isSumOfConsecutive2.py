def isSumOfConsecutive2(n):
    counter = 0
    L = 1
    while( L * (L + 1) < 2 * n):
        a = (1.0 * n - (L * (L + 1) ) / 2) / (L + 1)
        if (a - int(a) == 0.0):
            counter += 1
        L += 1
    return counter