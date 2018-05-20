from math import floor
# All this question is asking to do it to find the median
def absoluteValuesSumMinimization(a):
    return a[len(a)//2 -1] if len(a) % 2 == 0 else a[floor(len(a) / 2)]
