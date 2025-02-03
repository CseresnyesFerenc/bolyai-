# szotar={"cat":"cica","dog":"kutya","horse":"ló"}
# words=['cat','lion','horse']
#
# for word in words:
#     if word in szotar:
#         print(word,"-->",szotar[word])
#     else:
#         print(f"A '{word}' nincs benne a szótárban")
#




# szotar={"cat":"cica",
#         "dog":"kutya",
#         "horse":"ló"}
#
# for key in szotar.keys():
#     print(key,"-->",szotar[key])




# szotar={"cat":"cica",
#         "dog":"kutya",
#         "horse":"ló"}
#
# szotar['cat']='macska'
# print(szotar)




# szotar={"cat":"cica",
#         "dog":"kutya",
#         "horse":"ló"}
#
# szotar['swan']='hattyú'
# szotar.update({"duck":"kacsa"})
# print(szotar)





# szotar={"cat":"cica",
#         "dog":"kutya",
#         "horse":"ló"}
#
# del szotar['cat']
# szotar.popitem()#csak az utolso elem
# print(szotar)





# szotar={"cat":"cica",
#         "dog":"kutya",
#         "horse":"ló"}
# for english, magyar in szotar.items():
#         print(english,'->',magyar)




# szotar={"cat":"cica",
#         "dog":"kutya",
#         "horse":"ló"}
# for magyar in szotar.values():
#         print(magyar)




# szotar={"cat":"cica",
#         "dog":"kutya",
#         "horse":"ló"}
# x=szotar.get("cat")
# print(x)
#


# szotar={"cat":"cica",
#         "dog":"kutya",
#         "horse":"ló"}
# x=szotar.copy()
# print(x)

def beker(_kulcs,_szoveg):
    ember={}
    for i in range(len(_kulcs)):
        ember[_kulcs[i]]=input(f"Kérem adja meg a {_szoveg[i]}:")
    return(ember)

kulcs=["név","Matek","Magyar","Töri"]
szoveg=["nevét","Matek jegyét","Magyar jegyét","Töri jegyét"]
osztaly=[]


for i in range(2):
    print(f"{i+1}.tanuló adatai")
    print(30*"-")
    osztaly.append(beker(kulcs,szoveg))
print(osztaly)
osszeg=0
for egy in osztaly:
    print(egy["név"])
    osszeg+=int(egy["Matek"])
db=len(osztaly)
print(f"Az osztály matek átlaga: {osszeg/db}")


