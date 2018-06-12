from functools import reduce

def mathPractice(numbers):
    return reduce(lambda x,y: (x+y[1] if y[0]%2 else x*y[1]), enumerate(numbers), 1)
