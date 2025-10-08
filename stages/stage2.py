def swap(x, y):
    x = x + y
    y = x - y
    x = x - y
    return (x, y)


swap(123, 456)
