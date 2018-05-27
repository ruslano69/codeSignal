def circleOfNumbers(n, firstNumber):
    return firstNumber - n/2 if (n/2 + firstNumber > n-1) else n/2 + firstNumber
