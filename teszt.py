x=float(input("Kerem adja meg a magasságát m-ben"))
y=float(input("Kérem adja meg a testömegét kg-ban:"))
print(20*"*",8*"-",20*"*")
print("Az ön testömeg indexe:", round(y/(x)**2,2),"%")
print("Az ön magasságához ideális testömeg:", round (18.5*(x)**2,2), "KG és", round(24.9*(x)**2,2), "KG között van")