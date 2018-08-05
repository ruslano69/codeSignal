def celsiusVsFahrenheit(yourTemps, friendsTemps):
    counter = 0
    for i in range(len(yourTemps)):
        your_temp_fahrenheit = 9 * yourTemps[i] / 5 + 32
        if your_temp_fahrenheit < friendsTemps[i]:
            counter += 1
    return counter
    