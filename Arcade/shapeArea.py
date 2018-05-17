def shapeArea(n):
    # Area is initially 1
    area = 1
    for index in range(n):
        area += 4*(index)
    return area