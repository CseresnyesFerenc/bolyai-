a=int(input("Kérem adja meg a háromszög 'a' oldalának hosszát: "))
b=int(input("Kérem adja meg a háromszög 'b' oldalának hosszát: "))
c=int(input("Kérem adja meg a háromszög 'c' oldalának hosszát: "))

if c<a+b and c+a>b and a<b+c:
    print("A háromszög létrehozható")
    s = (a + b + c) / 2
    print("A háromszög kerülete: ", s, ("A háromszög területe:"), (s * (s - a) * (s - b) * (s - c) ** 0.5))

else:
    while c>a+b or c+a<b or a>b+c:
        print("A háromszög nem léhetéges")
        a = int(input("Kérem adja meg a háromszög 'a' oldalának hosszát: "))
        b = int(input("Kérem adja meg a háromszög 'b' oldalának hosszát: "))
        c = int(input("Kérem adja meg a háromszög 'c' oldalának hosszát: "))
if c<a+b and c+a>b and a<b+c:
    print("A háromszög létrehozható")
    s = (a + b + c) / 2
    print("A háromszög kerülete: ", s, ("A háromszög területe:"), (s * (s - a) * (s - b) * (s - c) ** 0.5))

