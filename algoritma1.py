liste = [11, 28, 76, 57, 202]
max=max(liste[0],liste[1])

for i in range(2,len(liste)):
    if liste[i]>max:
        secondmax=max
        max=liste[i]
    else:
        if liste[i]>secondmax:
            secondmax=liste[i]

print("ikinci en büyük sayı: ", str(secondmax))