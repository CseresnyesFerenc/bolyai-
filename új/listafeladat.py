t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=['Január', 'Február', 'Március', 'Április', 'Május', 'Június',  'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
t3=[]
for i in range(12):
    t3.append(t2[i])
    t3.append(t1[i])
print(t3)
hossz=len(t2)
for i in range(hossz):
    if i!=hossz-1:
        print(t2[i]+"*",end='')
    else:
        print(t2[i])

