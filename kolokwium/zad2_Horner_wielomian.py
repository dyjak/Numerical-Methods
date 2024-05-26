if __name__ == '__main__':
    print("*** f(x) : g(x) = h(x) * g(x) ***\n")

    n=2
    f_x = [2, 3, 4]

    print("\nWielomian f(x): ")
    print("f(x) = ", end='')
    for i in range(n, -1, -1):
        print(str(f_x[i]) + "x^" + str(i), end='')
        if i != 0:
            print(' + ', end='')

    g_x = [2, 1] #x + 2
    print("\nDwumian g(x): ")
    print("g(x) = " + str(g_x[1]) + "x + " + str(g_x[0]), end='')

    gx0 = (g_x[0] / g_x[1])
    if (g_x[1] * g_x[0] * gx0) > 0 : gx0 *= -1
    print("\nx zerujący g(x):\tx = " + str(gx0))

    h_x: list[int] = [0] * (n + 1)
    h_x[n] = f_x[n]
    for i in range(n - 1, -1, -1):
        h_x[i] = gx0 * h_x[i + 1] + f_x[i]

    print("\nWielomian h(x):")
    print("h(x) = ", end='')
    for i in range(n, 0, -1):
        print(str(h_x[i]) + "x^" + str(i - 1), end='')
        if i != 1:
            print(' + ', end='')
    print('\nR = ' + str(g_x[0]))
