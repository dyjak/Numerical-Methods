if __name__ == '__main__':
    print("*** Schemat Hornera f(x) w punkcie x0 ***\n")


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


    print("\n\nImplementacja punktu x0: ")
    x0=int(input())


    wsp3 : list[int] = [0] * (st1+1)
    wsp3[st1]=wsp1[st1]
    for i in range(st1-1, -1, -1):
        wsp3[i] = x0*wsp3[i+1] + wsp1[i]


    print("\nWartość f(x) w punkcie x0: " + str(wsp3[0]))

