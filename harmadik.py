
# szoveg="k"
# while szoveg!="alma":
#     szoveg = input("kérek egy szót:")
# if szoveg == "alma":
#     print("eltalálta")
# else:
#     print("nem jó")
# print("vége")

print("indul a program:")
num1 = int(input("kérem adjon meg egy számocskát:"))
num2 = int(input("adja meg a második számocskát:"))
while num1<num2+1:
    if num1%2==0:
        print(num1)
    num1+=1
print("vége")