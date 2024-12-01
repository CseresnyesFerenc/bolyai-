print("1.feladat")
max=None
lista1=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]
negative=False
osszeg=None
print(len(lista1),"Darab elem van")
for i in range(len(lista1)):
    if lista1[i]<0:
        negative=True
        break

if negative:
    print("Van negatív")
else:
    print("nincs negatív")
for i in range(len(lista1)):
    if lista1[i]%2==0:
        count=len(lista1)
print("páros számok:", count)
igazsag=True
for num in lista1:
    if num >= 100:
        hazugsag=False
        break
if hazugsag:
    print("Minden szám kisebb 100-nál.")
else:
    print("Nem minden szám kisebb 100-nál.")
oszthato = None
for i in range(len(lista1)):
    if lista1[i] % 3 == 0 and lista1[i] % 5 == 0:
        oszthato=lista1[i]
        break

if oszthato!=None:
    print("Az első 3-mal és 5-tel is osztható szám:", oszthato)
else:
    print("Nincsenek 3-al vagy 5-el osztható számok")


masodik=False
for num in lista1:
    if num>=0:
        if round(num**(1/3))**3==num:
            masodik=True
            break
if masodik:
    print("Van köbszám a sorozatban.")
else:
    print("Nincs köbszám a sorozatban.")

for num in lista1:
    if num >= 0 and (num ** 0.5).is_integer():
        print("A szám:", num , "Négyzetgyöke:",int(num ** 0.5))
found=False
for i in range(len(lista1)-1):
    if lista1[i]>0 and lista1[i+1]==0:
        found=True
        break


if found:
    print("Van pozitív szám, amit nulla követ.")
else:
    print("Nincs olyan pozitív szám, amit nulla követ.")
for num in lista1:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print("Prím szám:",num)
first_max = second_max = float('-inf') #float('-inf') az alapértelmezett legnagyobb érték

for num in lista1:
    if num>first_max:
        second_max=first_max
        first_max=num
    elif num>second_max and num!=first_max:
        second_max=num #num az egy külső eszköz a pythonhoz, a matematikai műveletek kezeléséhez


print("A második legnagyobb szám:",second_max)
