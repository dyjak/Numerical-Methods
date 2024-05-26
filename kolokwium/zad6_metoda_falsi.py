# warunki: warunek Cauchyego, f'(x0)*f''(x0)>0 [x0 = a lub b], ciągłość pochodnych na przedziale

import math
import sympy as sp

x = sp.symbols('x')

f_x = 3*x - sp.cos(x) - 1  # dana funkcja

def f(x0):
    return f_x.subs(x, x0)

def fp(x0): #pierwsza pochodna
    d = sp.diff(f_x, x)
    #print(d)
    return d.subs(x, x0)

def fpp(x0): #druga pochodna
    dd = sp.diff(sp.diff(f_x, x), x)
    # print(dd)
    return dd.subs(x, x0)


def warunekCauchyego(a, b):
    return True if f(a) * f(b) < 0 else False


def warunekPochodnych(a, b):
    if fp(a) * fpp(a) > 0:
        return a
    elif fp(b) * fpp(b) > 0:
        return b
    else:
        return False



def x_i(a, b): #i-ty wyraz rekurencji
    x_i = a - (f(a) * (b - a)/(f(b) - f(a)))
    return x_i




if __name__ == '__main__':
    a = 0.25
    b = 0.75
    E = 0.00001 #dokładność

    if ( (not warunekPochodnych(a, b)) or (not warunekCauchyego(a, b)) ) :
        print("Kryteria nie spełniają warunków początkowych. Koniec zadania.")
    else:
        x0 = warunekPochodnych(a, b)
        i = 1
        while (abs(f(x0)) > E):
            print("obrót", i, ":")
            i = i + 1
            x0 = x_i(a, b)
            print("a =", a, "\nb =", b, "\nx_i =", x0)
            f_c = f(x0)
            print("f(a) =", f(a))
            print("f(b) =", f(b))
            print("f(x_i) =", f_c, "\n")

            if (warunekCauchyego(a, x0)):
                b = x0
            elif (warunekCauchyego(x0, b)):
                a = x0
            else:
                print("Koniec możliwości.")

        print("\n\nRozwiązanie: x = ", x0)


