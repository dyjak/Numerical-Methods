#   f(x) = ax^3 + bx^2 + cx + d
import sympy as sp


x = sp.symbols('x')
a = sp.symbols('a')
b = sp.symbols('b')
c = sp.symbols('c')
d = sp.symbols('d')

def f(points_x, points_y):
    n = len(points_x)
    suma=0
    for i in range(n):
        suma +=  (a*points_x[i]**3 + b*points_x[i]**2 + c*points_x[i] + d - points_y[i])**2
    return sp.simplify(suma)

def aproxymacja(f):
    derivative_a = sp.diff(f,a)
    derivative_b = sp.diff(f,b)
    derivative_c = sp.diff(f,c)
    derivative_d = sp.diff(f,d)
    print("Pochodne cząstkowe:")
    print("\t",derivative_a, "= 0")
    print("\t",derivative_b, "= 0")
    print("\t",derivative_c, "= 0")
    print("\t",derivative_d, "= 0")
    derivatives = [derivative_a, derivative_b, derivative_c, derivative_d]

    solutions = sp.solve(derivatives, (a, b, c, d))
    print("Rozwiązania: ", sp.simplify(solutions))

    return f"funkcja aproksymująca: {solutions[a]}*x^3 + {solutions[b]}*x^2 + {solutions[c]}*x + {solutions[d]}"


if __name__ == '__main__':
    print("f(x) = ax^3 + bx^2 + cx + d")

    points_x=[0,3,6,9]
    points_y=[4,5,4,1]

    f = f(points_x, points_y)
    print("Funkcja bazowa: ", f)
    print(aproxymacja(f))

