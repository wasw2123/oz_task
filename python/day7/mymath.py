def ThiArea(w, h):
    area = w * h * 0.5
    return area

def CirArea(r):
    pi = 3.141592
    area = pi * r ** 2
    return area

def BoxSurArea(x, y, z):
    sur_area = ((x * y) + (y * z) + (z * x)) * 2
    return sur_area