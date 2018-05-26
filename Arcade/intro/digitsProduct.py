def digitsProduct(product):
    if product < 10:
        return product if product > 0 else 10
    r = ""
    for i in range(9,1,-1):
        while product % i == 0:
            product /= i
            r = chr(ord('0')+i)  + r;
    return -1 if product != 1 else int(r)
