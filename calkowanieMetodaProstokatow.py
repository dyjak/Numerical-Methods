import math


def f(x):
    return 0.06 * (x**2) + 2


def poleProstokata(a, b):
    return (b-a) * f(b)


def calka(x_p, x_k, n):
    h = (x_k - x_p) / n  # przeskok
    suma = 0
    for i in range(0, n):
        print("\n", i + 1, ":")
        print("a = ", x_p, "\tb = ", x_p + h)
        print("pole prostokąta = ", poleProstokata(x_p, x_p + h))
        suma += poleProstokata(x_p, x_p + h)
        x_p += h
        print("suma = ", suma)
    return suma


if __name__ == '__main__':
    x_p = 1
    x_k = 4
    n = 9
    print(calka(x_p, x_k, n))
