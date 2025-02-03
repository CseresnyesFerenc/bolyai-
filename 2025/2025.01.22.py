eu = open("eu.csv", 'r', encoding='utf-8')
tagok = []
for elem in eu:
    elem = elem.strip().split(",")
    tagok.append(elem)

print(tagok)

egy_orszag = {"orszag"}

print("Városok")
for elem in tagok:
    print(elem[1], end=",")

print("Évszámok")
ev = []
for elem in tagok:
    ev.append(elem[2])
alapitas = min(ev)
szamlalo = 0
for elem in tagok:
    if elem[2] == alapitas:
        szamlalo += 1
print(f"Az EU-t {szamlalo} db ország alapította")
for elem in tagok:
    rovid = tagok[0][0]
    len(rovid) > len(elem[0])
    rovid = elem[0]
