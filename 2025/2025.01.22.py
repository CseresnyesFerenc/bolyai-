eu=[]
with open('eu.csv','r',encoding='utf-8') as forras:
    for sor in forras:#"Dánia,Koppenhága,1973 "
        orszag=sor.strip().split(",")
        eu.append(orszag)