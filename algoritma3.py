def tekrar(x):
    size = len(x)
    tekrarlanan = []
    for i in range (size) :
        k = i + 1
        for j in range(k, size) :
            if x[i] == x[j] and x[i] not in tekrarlanan:
                tekrarlanan.append(x[i])
    return tekrarlanan

liste = [18, 59, 40, 5, 99, 40]
print("Tekrarlanan sayı: ", tekrar(liste))                