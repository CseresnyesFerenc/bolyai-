elso=float(input("kérem adjon meg az első számot:"))
masodik=float(input("kérem adja meg a második számot:"))
print("A két számod összege:",elso+masodik)
a=float(input("kérem adja meg a téglalap A oldalát:"))
b=float(input("kérem adja meg a téglalap B oldalát:"))
print("A téglalap kerülete",2*(a+b))
print("A téglalap területe:",a*b)

szo=input("Ez nagyon szép szó:")
if szo=="tűzliliom":
    print("Ezt ismerem, ez egy csodaszép virág")
else:
    print("ez egy szép szó")




fizetes=float(input("kérem adja meg a fizetését:"))
if fizetes<14400:
    print("nem kell adózni")
    print("keresett",fizetes,"Euro")
