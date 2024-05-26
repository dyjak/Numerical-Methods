import math
# Definiujemy funkcję, którą będziemy całkować
def f(x):
    return math.sin(x) * math.exp(-3 * x) + x**3
# Definiujemy funkcję, którą będziemy całkować
def simpson_rule(a, b, n):
    # Obliczamy krok całkowania
    h = (b - a) / n
    # Inicjalizujemy wartość całki wartościami funkcji na końcach przedziału
    integral = f(a) + f(b)
    # Iterujemy przez wszystkie parabole z nieparzystymi indeksami
    for i in range(1, n, 2):
        # Dodajemy do całki 4 razy wartość funkcji w środku paraboli
        integral += 4 * f(a + i * h)
        # Iterujemy przez wszystkie parabole z parzystymi indeksami
    for i in range(2, n, 2):
        # Dodajemy do całki 2 razy wartość funkcji na końcach paraboli
        integral += 2 * f(a + i * h)
    # Mnożymy sumę przez krok całkowania podzielony przez 3 i zwracamy wynik
    integral *= h / 3
    return integral
# Dolna granica całkowania
a = -3
# Górna granica całkowania
b = 1
# Liczba parabol
n = 1000

wynik = simpson_rule(a, b, n)
print(f"Wartość całki: ", wynik)