def alternatingSums(a):
    sum01, sum02 = 0, 0 
    for index in range(len(a)):
        if index % 2 == 0:
            sum01 += a[index]
        else:
            sum02 += a[index]
    return [sum01, sum02]