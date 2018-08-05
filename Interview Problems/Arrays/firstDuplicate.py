def firstDuplicate(a):
    found = {}
    for num in a:
        if num in found:
            return num
        else:
            found[num] = 1
    return -1