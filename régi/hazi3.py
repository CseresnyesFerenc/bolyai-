oktet1=int(input("Add meg az első oktetet: "))
oktet2=int(input("Add meg a második oktetet: "))
oktet3=int(input("Add meg a harmadik oktetet: "))
oktet4=int(input("Add meg a negyedik oktetet: "))
b1=""
b2=""
b3=""
b4=""
for i in range(8):
    b1 = str(oktet1%2)+b1
    oktet1 = oktet1//2
    b2 = str(oktet2%2)+b2
    oktet2 = oktet2 // 2
    b3 = str(oktet3 % 2)+b3
    oktet3 = oktet3//2
    b4 = str(oktet4 % 2)+b4
    oktet4 = oktet4//2
print("Bináris formátum:"+b1+"."+b2+"."+b3+"."+b4)
ip=input("Add meg az IPv4 címet (pl. 192.168.1.1): ")
oktets=ip.split('.')
oktet1=int(oktets[0])
oktet2=int(oktets[1])
oktet3=int(oktets[2])
oktet4=int(oktets[3])
b1=""
b2=""
b3=""
b4=""
for i in range(8):
    b1=str(oktet1%2)+b1
    oktet1=oktet1//2
    b2=str(oktet2%2)+b2
    oktet2=oktet2//2
    b3=str(oktet3%2)+b3
    oktet3=oktet3//2
    b4=str(oktet4%2)+b4
    oktet4=oktet4//2
print("Bináris formátum: "+ b1 + "." + b2 + "." + b3 + "." + b4)
