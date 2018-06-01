def magicalWell(a, b, n):
    money = 0
    for _ in range(n):
        money += a*b
        a += 1
        b += 1
    return money