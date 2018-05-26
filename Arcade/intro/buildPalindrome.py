def buildPalindrome(st):
    i = 0
    while st[i:] != st[i:][::-1]:
        i += 1
        if i == len(st):
            break
    st += st[:i][::-1]
    
    return st