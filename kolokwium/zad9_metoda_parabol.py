# calka 1, -3 sin(x) * e^-3x + x^3
import sympy as sp

import math

def f(x):
    return math.sin(x)*math.e**(-3*x) + x**3


def calka(a, b, n):
    h = (b - a) / n  # przeskok
    suma = f(a) + f(b)
    for i in range(1, n, 2):
        print("\nobrót: ", i + 1, ":")
        print("a = ", a, "\tb = ", a + h)
        poleParaboli = 4 * f(a)
        print("pole paraboli = ", poleParaboli)
        suma += poleParaboli
        a += h
    for i in range(2, n, 2):
        suma += 2*(f(a))
        a+=h

    print("\n(???)Rozwiązanie: ", suma)
    return suma


def blad_maksymalny(a, b, n):
    h = (b - a) / n
    x = sp.symbols('x')
    f_x = sp.sin(x)*math.e**(-3*x) + x**3
    d = sp.diff(f_x, x)
    dd = sp.diff(d, x)
    ddd = sp.diff(dd, x)
    dddd = sp.diff(ddd, x)
    return ((b - a) * h**4 * dddd.subs(x, a)) / 180



if __name__ == '__main__':
    a = -3
    b = 1
    n = 1000
    calka(a, b, n)
    print("błąd maksymalny: E = ",float(blad_maksymalny(a, b, n)))