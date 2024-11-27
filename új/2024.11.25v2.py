print("1.feladat")
max=None
lista1=[14,23,1,48,43,28,77,33,95,38,9,98,61,58,21,87,41,65,22,20,56,75,80,77,100,67,22,8,78,6]
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
