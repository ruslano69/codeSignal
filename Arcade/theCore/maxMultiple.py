def maxMultiple(divisor, bound):
    MyL = list()
    for i in range(bound+1):
        if i % divisor == 0 and i > 0:
            MyL.append(i)
    return MyL[-1]
