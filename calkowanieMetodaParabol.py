# calka 1, -3 sin(x) * e^-3x + x^3
import sympy as sp


import math

def f(x):
    return math.sin(x)*math.e**(-3*x) + x**3

def poleParaboli(a, b, h):
    return (h / 3) * (f(a) + 4 * f((a + b) / 2) + f(b))

def calka(x_p, x_k, n):
    h = (x_k - x_p) / n  # przeskok
    suma = 0
    for i in range(0, n):
        print("\n", i + 1, ":")
        print("a = ", x_p, "\tb = ", x_p + h)
        print("pole parabol = ", poleParaboli(x_p, x_p + h, h))
        suma += poleParaboli(x_p, x_p + h, h)
        x_p += h
        print("suma = ", suma)
    return suma

def blad_maksymalny(x_p, x_k, n):
    h = (x_k - x_p) / n
    M4 = sp(sp(sp(sp(x_p))))
    return ((x_k - x_p) * h**4 * M4) / 180

if __name__ == '__main__':
    x_p = -3
    x_k = 1
    n = 10
    print(str(calka(x_p, x_k, n)),"+",str(blad_maksymalny(x_p, x_k, n)))