szuletesi_datum = input("Kérem adja meg a születési dátumát: ")

osszeg = 0
for karakter in szuletesi_datum:
    if '0' <= karakter <= '9':
        osszeg += int(karakter)

while osszeg >= 10:
    uj_osszeg = 0
    for szamjegy in str(osszeg):
        uj_osszeg += int(szamjegy)
    osszeg = uj_osszeg

print("Az élet számjegye:", osszeg)
