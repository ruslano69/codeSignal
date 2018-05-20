def circleOfNumbers(n, firstNumber):
    num = firstNumber
    for i in range(n//2):
        num += 1
        if num == n:
            num = 0
    return num