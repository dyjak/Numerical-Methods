import numpy as np

def gauss(A, b):
    """
    Funkcja wykonująca eliminację Gaussa w celu rozwiązania układu równań liniowych Ax = b.

    Parametry:
        A (numpy.array): Macierz współczynników.
        b (numpy.array): Wektor wyrazów wolnych.

    Zwraca:
        x (numpy.array): Wektor rozwiązania.
    """
    n = len(b)  # Liczba niewiadomych/rozmiar macierzy
    A = A.astype(float)  # Konwersja na liczby zmiennoprzecinkowe dla dokładności
    b = b.astype(float)
    # Eliminacja współczynników poniżej głównej przekątnej
    for i in range(n):
        # Wybór głównego elementu (elementu największego bezwzględnie) w kolumnie
        max_row = np.argmax(abs(A[i:n, i])) + i
        # Zamiana wierszy, aby umieścić maksymalny element na głównej przekątnej
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Eliminacja kolejnych współczynników
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]  # Współczynnik do wyeliminowania elementu
            A[j, i:] -= factor * A[i, i:]  # Eliminacja elementów w bieżącym wierszu
            b[j] -= factor * b[i]  # Korekta elementu w wektorze wyrazów wolnych

    # Rozwiązanie równań za pomocą wstecznej substytucji
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


if __name__ == '__main__':
    # Przykładowe równanie
    A = np.array([[3, 0, 6],
                  [1, 2, 8],
                  [4, 5, -2]])

    b = np.array([-12, -12, 39])

    # Rozwiązanie układu równań
    x = gauss(A, b)
    print("Rozwiązanie x:", x)