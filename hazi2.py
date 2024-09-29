n=int(input("Adj meg egy természetes egész számot:"))
i=0
print(n)
while n!=1:
    if n%2==0:
        n=n// 2
    else:
        n=n+1
    i=i+1
    print(n)
print("összeg:",i)
