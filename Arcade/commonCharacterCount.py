def commonCharacterCount(s1, s2):
    counter = 0
    s1Chars = list(s1)
    s2Chars = list(s2)
    for char in set(s1Chars):
        if char in s2Chars:
            counter += s1Chars.count(char) if s1Chars.count(char) < s2Chars.count(char) else s2Chars.count(char)
        
    
    return counter
