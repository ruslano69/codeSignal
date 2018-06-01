def increaseNumberRoundness(n):
    isZeroInMiddle = False
    for char in str(n):
        if isZeroInMiddle and char != "0":
            return True
        if char == "0":
            isZeroInMiddle = True
    return False
