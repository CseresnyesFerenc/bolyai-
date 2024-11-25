szamlalo=0
van=False
t=[]
vmi=None
osszeg=0
while vmi!=0:
    vmi=int(input("Kérem adjon megy egy számot, ha ki akar lépni adjon meg egy 0-t: "))
    t.append(vmi)
print(t)
MaxElem=t[0]
for elem in t:
    print(elem, MaxElem)
    if elem>MaxElem:
        MaxElem=elem
    osszeg=osszeg+elem
    if elem<5:
        szamlalo+=1
    if elem%2==0:
        van=True
print("Az ötnél kisseb számok:",szamlalo)
print("legnagyobb elem: ",MaxElem)
print("Összeg:",osszeg)
print("A páros számok:",)
#Meg kell tanulni:
# maximum (érték)
# max(hely)
# összegzés
# min(érték)
# min(hely
# megszámlálás
# eldöntés
# kiválasztás
# keresés
# kiválogatás
# szétváloga
