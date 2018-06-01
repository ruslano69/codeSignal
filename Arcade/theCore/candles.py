def candles(candlesNumber, makeNew):
    totalCandles = 0
    leftovers = 0
    while candlesNumber > 0:
        totalCandles += candlesNumber
        leftovers += candlesNumber
        candlesNumber = leftovers // makeNew
        leftovers %= makeNew
    return totalCandles
