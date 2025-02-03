print("I.Feladat")
print(1000*"-")
num1 = int(input("Kérem adjon meg egy számot: "))
num2 = int(input("Kérem adjon meg még egy számot: "))
if num1 > num2:
    print("Az első szám nagyobb!")
if num2 > num1:
    print("A Második szám nagyobb!")
if num1 == num2:
    print("A két szám egyenlő!")
print("I.Feladat")
print(1000 * "-")


def kodolas(szoveg, betu, szam):

    ujszoveg = ""
    szamlalo = None
    for egy in szoveg:
        if egy == betu and szamlalo < szam:
            szamlalo += 1
            egy = str(ord(egy))
        ujszoveg += egy
    return ujszoveg


print(kodolas("Valami szöveget írtam be", "a", 2))
