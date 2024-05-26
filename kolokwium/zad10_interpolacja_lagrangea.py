import sympy as sp

x = sp.symbols('x')

def lagrange(points_x, points_y):
    n = len(points_x)
    suma = 0
    for i in range(n):
        mul1 = points_y[i]
        mul2 = 1
        for j in range(n):
            if j != i:
                mul1 *= (x-points_x[j])
                mul2 *= (points_x[i] - points_x[j])
        suma += mul1/mul2
    return sp.simplify(suma)


if __name__ == '__main__':
    points_x = [1, 2, 3]
    points_y = [5, 7, 6]
    print(lagrange(points_x, points_y))
