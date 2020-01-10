def pairs (liste, n, toplam) :
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (liste[i] + liste [j] == toplam):
                 print("(", liste[i],  
                      ", ", liste[j],  
                      ")", sep = "")

liste = [10, 3, 4, 5, -3, 2, 9]
n = len(liste)
toplam = 7
pairs(liste, n, toplam)                      
