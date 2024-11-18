def beker(szoveg,szam):
    jegyek = []
    jegy = int(input("Kérem adja meg a "+szoveg+" jegyet:"))
    while jegy != 0:
        jegyek.append(jegy)
        jegy = int(input("Kérem adja megy a "+szoveg+" jegyet (1-5): "))
    return atlag(jegyek)

def atlag(lista):
    hossz = len(lista)
    vissza = 0
    for i in range(hossz):
        vissza = vissza + lista[i]

    return round(vissza/hossz ,1)


#******************************************************************************************************
matek = 0
tori = []
magyar = []

matek = beker("Magyar", 2)

# tori = beker("Tori")
# magyar = beker("Magyar")
print("Matek:", matek)
# print("Tori:", tori)
# print("Magyar:", magyar)


