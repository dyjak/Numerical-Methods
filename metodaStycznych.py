# f(x) = sin(x) - 1/2x - funkcja

import math
import sympy as sp


def f(x):
    return math.sin(x) - (1 / 2) * x


def fp(x):
    return math.cos(x) - 1 / 2


def fpp(x):
    return -math.sin(x)


def x_i(x_p, x_k):
    x = x_k - (f(x_k) / fp(x_k))
    return x


def warunekCauchyego(x_p, x_k):
    return True if f(x_p) * f(x_k) < 0 else False


def warunekPoczatkowy(x_p, x_k):
    if f(x_p) * fpp(x_p) > 0:
        return x_p
    elif f(x_k) * fpp(x_k) > 0:
        return x_k
    else:
        return False


def warunekPochodnych(x_p, x_k):
    if f(x) * sp.diff(sp.diff(f(x_p))) > 0: return True
    elif f(x) * sp.diff(sp.diff(f(x_k))) > 0: return True
    else: return False


if __name__ == '__main__':
    x_p = math.pi / 2
    x_k = math.pi
    E = 0.001
    if warunekPoczatkowy(x_p, x_k):
        f_c = warunekPoczatkowy(x_p, x_k)

        i = 1  # obroty
        while (abs(f_c) > E and warunekCauchyego(x_p, x_k) and warunekPoczatkowy(x_p, x_k)):  # ????
            print(i, ":")
            i = i + 1
            x = x_i(x_p, x_k)
            print("x_p =", x_p, "\nx_k =", x_k, "\nx_i =", x)
            f_c = f(x)
            print("f(x_p) =", f(x_p))
            print("f(x_k) =", f(x_k))
            print("f(x_i) =", f_c, "\n")

            if (warunekCauchyego(x_p, x)):
                x_k = x
            elif (warunekCauchyego(x, x_k)):
                x_p = x
            else:
                print("Koniec możliwości, żegnam")
    else:
        print("Mamy problem.")
