radio=[]
radiosok=open("cb.txt",'r', encoding='utf-8')
radiosok.readline(383)
for elem in radiosok:
    elem=elem.strip().split(";")
    radio.append(elem)
print(radio)
print("I.feladat")
nev=[]
for elem in radio:
    if elem[3] not in nev:
        nev.append(elem[3])
print(f"A rádiosok száma: {len(nev)}, neveik: {nev}")
print("II.Feladat")
adas=[]
for elem in radio:
    if elem[2] not in adas:
        adas.append(elem[2])
print(adas)