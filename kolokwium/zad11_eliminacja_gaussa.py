def gauss(A, b):
    n = len(A)  # rozmiar macierzy A
    M = A  # macierz pomocnicza

    # Dodajemy wektor b do macierzy M
    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):
        # szukamy wiersza z największym elementem w kolumnie
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        # przechodzimy przez każdy wiersz poniżej obecnego
        for j in range(k+1, n):
            # Obliczamy współczynnik
            q = float(M[j][k]) / M[k][k]
            # aktualizujemy wiersz
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    # inicjalizujemy wektor rozwiązania
    x = [0 for i in range(n)]

    # obliczamy rozwiązanie
    x[n-1] = float(M[n-1][n]) / M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z + float(M[i][j]) * x[j]
        x[i] = float(M[i][n] - z) / M[i][i]
    return x


def lu(A):
    n = len(A)  # rozmiar macierzy A
    L = [[0.0] * n for i in range(n)]  # macierz L
    U = [[0.0] * n for i in range(n)]  # macierz U

    for i in range(n):
        # przechodzimy przez każdą kolumnę wiersza
        for j in range(i, n):
            # obliczamy sumę iloczynów dla macierzy U
            sum1 = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - sum1

        # przechodzimy przez każdą kolumnę wiersza
        for j in range(i, n):
            if i == j:
                L[j][i] = 1.0  # diagonalne elementy macierzy L są równe 1
            else:
                # obliczamy sumę iloczynów dla macierzy L
                sum2 = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (A[j][i] - sum2) / U[i][i]

    return L, U

A = [[3, 0, 6], [1, 2, 8], [4, 5, -2]]
b = [-12, -12, 39]  # wektor b

L, U = lu(A)
print("macierz L: ", L)
print("macierz U: ", U)

print("Rozwiązanie metodą eliminacji Gaussa: ", gauss(A, b))