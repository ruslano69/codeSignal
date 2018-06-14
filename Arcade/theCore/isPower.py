def isPower(n):
    if n == 1:
        return True
    for val in range(2,n):
        temp = n
        while (n%val == 0):
            n /= val
        if n == 1:
            return True
        n = temp
    return False