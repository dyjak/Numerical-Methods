import sympy as sp

x = sp.symbols('x')

#sample function
# f_x = sp.simplify(x-2)
# print(f_x)


def lagrange(points_x, points_y):
    n = len(points_x)
    sum = 0
    for i in range(n):
        mul1 = points_y[i]
        mul2 = 1
        for j in range(n):
            if j != i:
                mul1 *= (x-points_x[j])
                mul2 *= (points_x[i] - points_x[j])
        sum += mul1/mul2
    return sp.simplify(sum)

# def newton(points_x, points_y):


if __name__ == '__main__':
    points_x = [1,2,3]
    points_y = [5,7,6]
    print(lagrange(points_x, points_y))
