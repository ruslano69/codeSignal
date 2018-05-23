def growingPlant(upSpeed, downSpeed, desiredHeight):
    growth = 0
    days = 0
    while growth < desiredHeight:
        days += 1
        growth += upSpeed
        if growth < desiredHeight:
            growth -= downSpeed
    return days
