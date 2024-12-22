def dobav(a,b):
    return a+b

def vichti(a,b):
    return a-b

def razdeli(a,b):
    if b == 0:
        raise ValueError("Делить на ноль нельзя.")
    return a/b

def umnozh(a,b):
    return a*b