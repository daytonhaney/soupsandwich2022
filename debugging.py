def getArea(l, w):
    area = l * w
    print(f"Area is {area}")
    price_per_square = float(2.00)
    total_price = area * price_per_square
    print(total_price)

    return total_price, area, price_per_square


total_price = getArea(15, 3)
