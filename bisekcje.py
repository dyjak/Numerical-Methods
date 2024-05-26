def warunekCauchyego(wielomian, przedzial) :

    f_a = f_wPunkcie(wielomian, przedzial[0])
    f_b = f_wPunkcie(wielomian, przedzial[1])

    print("przedział: [" + str(przedzial[0])+", " + str(przedzial[1]) + "]\nf(a) = " + str(f_a) + "\t f(b) = "+str(f_b))
    print("f(a) * f(b) = "+str(f_a*f_b) + ("\tspełniony" if ((f_a*f_b)<0) else "\tniespełniony"))
    return True if f_a * f_b < 0 else False



def f_wPunkcie(wielomian, punkt) :
    wartosc=0
    for i in range (len(wielomian)) :
        wartosc+=wielomian[i]* pow(punkt, i)
    return wartosc



if __name__ == '__main__':    #c  x  x2 x3
    wielomian : list [int] = [-1, 1, 0, 1]
    przedzial : list [int] = [0, 1]
    E = 0.01
    f_c=1 #losowa wartość większa od E

    while(f_c > E or f_c < E and warunekCauchyego(wielomian, przedzial)) :
            print("\n1.")
            warunekCauchyego(wielomian,przedzial)
            c=(przedzial[0]+przedzial[1])/2
            print("c = ", c)
            f_c = f_wPunkcie(wielomian, c)
            print("f(c) = ", f_c)
            if f_wPunkcie(wielomian,c)*f_wPunkcie(wielomian,przedzial[1])<0 : przedzial=[c, przedzial[1]]
            elif f_wPunkcie(wielomian,c)*f_wPunkcie(wielomian,przedzial[0])<0 : przedzial=[przedzial[0], c]
            else : print("???")

    print("\n\n", (f_c > E), (f_c*(-1) < E), (warunekCauchyego(wielomian, przedzial)))
