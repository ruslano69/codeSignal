from fractions import gcd
def countBlackCells(n, m):
    return n + m + gcd(n,m) - 2
