def uzen():
    print("kérem adjon meg egy számot: ", end="")
def osszeg(a,b,c):
    osszead=(a+b+c)
#**************************************************************************************************************************************************************************************************************************************
for i in range(3):
    szamok = []
    osszeg = 0
    uzen()
    szam=int(input())
    osszeg+=szam
    szamok.append(szam)
print(f"A számok összege: {osszeg}")
osszeg(1,2,3)
