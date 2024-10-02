
n1=int(input("Írj be egy pozitív egész számot: "))


o=1
on=0


while o<=n1:
    if n1%o==0:
        print("A",o,"osztója a",str(n1)+"-nek")
        on+=1
    o+=1


if on==2:
    print("A",n1,"prímszám.")

