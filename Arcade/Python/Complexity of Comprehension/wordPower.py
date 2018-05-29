def wordPower(word):
    num = {char: ord(char)-96 for char in word.lower()}
    return sum([num[ch] for ch in word])
