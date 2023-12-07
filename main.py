import math

x = lambda z: z**2 + 3
y = lambda: math.sin(4)
function = lambda x, y: x + y

print(function(x(int(input())), y()))
