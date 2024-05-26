if __name__ == '__main__':

    n = 2 #stopień wielomianu
    f_x = [2, 3, 4] #4x^2 + 3x + 2

    print("\nWielomian f(x): ")
    print("f(x) = ",end='')
    for i in range(n, -1, -1):
        print(str(f_x[i])+"x^"+ str(i), end='')
        if i!=0:
            print(' + ', end='')


    print("\n\nPunkt x0: ")
    x0=int(input())


    g_x : list[int] = [0] * (n+1)
    g_x[n]=f_x[n]
    for i in range(n-1, -1, -1):
        g_x[i] = x0*g_x[i+1] + f_x[i]


    print("\nWartość f(x) w punkcie x0: " + str(g_x[0])) #reszta

