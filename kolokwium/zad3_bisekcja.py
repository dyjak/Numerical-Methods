#warunki: warunek Cauchyego
def f(x):
    f_x = [-1, 1, 0, 1] #f(x) = x^3 + x - 1
    suma = 0
    for i in range(len(f_x)):
        suma += f_x[i] * pow(x, i)
    return suma

def warunekCauchyego(a, b):
    f_a = f(a)
    f_b = f(b)
    print("przedział: [" + str(a) + ", " + str(b) + "]\nf(a) = " + str(f_a) + "\t f(b) = " + str(f_b))
    print("f(a) * f(b) = " + str(f_a * f_b) + ("\tspełniony" if ((f_a * f_b) < 0) else "\tniespełniony"))
    return True if f_a * f_b < 0 else False

if __name__ == '__main__':
    a = 0   #przedział
    b = 1   #przedział
    E = 0.01 # dokładność
    f_c = 1  # losowa wartość większa od |E|

    i=1
    if not warunekCauchyego(a, b):
        print("Warunek Cauchyego niespełniony. Koniec zadania.")
    else:
        while abs(f_c) > E:
            print("\nobrót",str(i),":")
            c = (a + b) / 2
            f_c = f(c)
            print("c = ", c)
            print("f(c) = ", f_c)

            if f(c) == 0:
                print("c =", c)
                break
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c

            print("Nowy przedział [" + str(a) + ", " + str(b) + "]")
            i+=1

        print("\n\nRozwiązanie\nc =", c)
        print("f(c) =", f_c)
        print("Przedział: [" + str(a) + ", " + str(b) + "]")
        print("E =", E)
        print("Błąd całkowity: |f(c)| =", abs(f_c))