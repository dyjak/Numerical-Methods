if __name__ == '__main__':
    print("*** Schemat Hornera f(x) : g(x) = h(x) * g(x) ***\n")


    st1 = int(input("Podaj stopień wielomianu f(x): "))
    wsp1 : list[int] = [0] * (st1+1)
    for i in range(st1, -1, -1):
        print("Współczynnik x^{} *? : ".format(i), end='')
        wsp1[i]=int(input())

    print("\nWielomian f(x): ")
    print("f(x) = ",end='')
    for i in range(st1, -1, -1):
        print(str(wsp1[i])+"x^"+ str(i), end='')
        if i!=0:
            print(' + ', end='')


    print("\n\nImplementacja dwumianu g(x)")
    wsp2: list[int] = [0] * 2
    print("Współczynnik x^1 *? : ", end='')
    wsp2[1]=int(input())
    print("Współczynnik x^0 *? : ", end='')
    wsp2[0]=int(input())

    print("\nDwumian g(x): ")
    print("g(x) = "+str(wsp2[1])+"x + "+str(wsp2[0]),end='')

    gx0 = (wsp2[0] / wsp2[1])
    if (wsp2[1]*wsp2[0]*gx0)>0 : gx0*=-1
    print("\nx zerujący g(x):\tx=" + str(gx0))


    wsp3 : list[int] = [0] * (st1+1)
    wsp3[st1]=wsp1[st1]
    for i in range(st1-1, -1, -1):
        wsp3[i] = gx0*wsp3[i+1] + wsp1[i]

    print("\nWielomian h(x):")
    print("h(x) = ",end='')
    for i in range(st1, 0, -1) :
        print(str(wsp3[i])+"x^"+ str(i-1), end='')
        if i!=1:
            print(' + ', end='')
    print('\nR = '+str(wsp3[0]))

