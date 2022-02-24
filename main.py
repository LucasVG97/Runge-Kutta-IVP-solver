import numpy as numpy


# equation PVI - Return any equation that you wish to solve
def f(x, y):
    # return y - numpy.sin(x)
    return x - y + 2


# here you have to insert the initial state of your PVI
xk = 0
yk = 2

# interval definition

a = 0
b = 1

# subdivision number, you may run this script multiple times with different subdivision
n = 8

# steps
h = (b - a) / n

# arraylists
xi = [xk]
yi = [yk]

# Runge Kutta iteration

for i in range(n):
    K1 = f(xk, yk)
    K2 = f(xk + h, yk + h * K1)
    yk = yk + (K1 + K2) * (h / 2)
    xk = xk + h
    print(f"({round(xk, 9)}, {round(yk, 9)})")
    xi.append(round(xk, 9))
    yi.append(round(yk, 9))

print("xk")
print(xi)
print("yk")
print(yi)
