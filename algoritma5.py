def minik(liste, n) :
    print("-1, ", end="")

    for i in range (1,n):
        for j in range(i-1, -2, -1):
            if (liste [j] < liste[i]):
                print(liste[j],",",
                              end="")
                break
        if (j == -1):
            print("-1, ", end="")


liste = [1, 4, 2, 7, 22, 5]
n = len(liste)
minik(liste,n)                             