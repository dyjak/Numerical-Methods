import math

def f(x):
    return math.sqrt(x + 1)


def poleTrapezu(a, b, h):
    return ((f(a) + f(b)) / 2) * h


def calka(a, b, n):
    h = (b - a) / n  # przeskok
    suma = 0
    print("przeskok: ",h)
    for i in range(0, n):
        print("\nobrót: ", i + 1, ":")
        print("a = ", a, "\tb = ", a + h)
        print("pole trapezu = ", poleTrapezu(a, a + h, h))
        suma += poleTrapezu(a, a + h, h)
        a += h
        print("suma = ", suma)
    print("\nRozwiązanie: ", suma)
    return suma



if __name__ == '__main__':
    a = 0
    b = 1
    n = 3
    calka(a, b, n)
