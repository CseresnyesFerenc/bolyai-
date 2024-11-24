
def harommal_oszthatok(lista):
    darab=0
    for szam in lista:
        if szam %3==0:
            darab+=1
    return darab
szamok=[]

print("Adj meg számokat! A program befejezéséhez írd be, hogy 0.")

bemenet=input("Szám:")
while bemenet!="0":

    if bemenet[0]=="-":
        helyes=1  
        for i in range(1,len(bemenet)):
            if bemenet[i] not in"0123456789":
                helyes=0 
                break    #A brake az egy vezérlő utasítás, ami a ciklusokat azonnal megszakítja
        if helyes==1:
            szamok.append(int(bemenet))
        else:
            print("Ez nem egy szám, próbáld újra!")
   
    else:
        helyes=1  
        for i in range(len(bemenet)):
            if bemenet[i] not in "0123456789":
                helyes=0  
                break
        if helyes==1:
            szamok.append(int(bemenet))
        else:
            print("Ez nem egy szám, próbáld újra!")
    
    bemenet=input("Szám: ")


darab=harommal_oszthatok(szamok)


print("A bekért számok közül", darab, "darab osztható hárommal.")
