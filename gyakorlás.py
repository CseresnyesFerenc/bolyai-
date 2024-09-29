n1=int(input("Kérem adjon meg egy pozitív egész számot:"))
n2=int(input("Kérem adjon meg egy pozitív egész számot:"))
print("A következő számok párosak:",end="")
while n1<n2+1:
    if n1%2==0:
        print(str(n1)+"-",end="")
    if n2%2==0:

    n1+=1