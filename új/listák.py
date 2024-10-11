lista1=["alma","körte","1920"]
print(lista1[0])
hossza=len(lista1)
print(hossza)
for i in range(hossza):
    print(lista1[i])
lista2=[10,12,25,4,9,13]
ossz=0
for i in range(len(lista2)):
    ossz+=lista2[i]
print("A lista elemeinek összege:",ossz)
lista3=[]
seged=1
while seged!=0:
    seged=int(input("kérem adjon meg egy számot: "))
    lista3.append(seged)
print(lista3)
print(len(lista3))