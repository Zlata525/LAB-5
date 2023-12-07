import math
def x(z):
    return lambda: z ** 2 + 3
def y():
    return lambda: math.sin(4)
def f(x, y):
    print(x()+y())

z = int(input())
f(x(z), y())
